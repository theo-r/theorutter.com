---
title: Secretless Deployments to AWS using Github Actions and AWS CDK
date: "2022-03-01T22:12:03.284Z"
description: "Learn how set up an OIDC provider using the AWS CDK."
---

A couple of weeks ago I read a fantastic blog post called [Stop using static cloud credentials in GitHub Actions](https://www.leebriggs.co.uk/blog/2022/01/23/gha-cloud-credentials.html). The post talks about a common headache when deploying to public cloud providers 
using an external tool such as Github Actions; namely, the problem of granting your pipelines
permission to your cloud resources. A common pattern is to store the credentials of 
an AWS user as secrets which can be referenced by the pipeline. There are a number
of issues with this approach but the biggest is the associated security risk; a leak of
credentials with permission to deploy resources in the cloud would be no laughing matter.

Luckily, as the post lays out, there is another option which leverages a protocol called
OpenID Connect. In this post I'm going to walk through the steps to set up an OIDC provider
using the AWS CDK which will allow us to deploy to AWS using Github Actions with no secrets required.

The first thing we need is a CDK App. 
I'll be writing my App in Python but this example can be easily modifed into whichever supported language suits you best.
The first construct we create is a ```CfnOIDCProvider``` which is an identity provider
that can be used as a principal in a role’s trust policy.

```python
cfn_oidc_provider = iam.CfnOIDCProvider(
    self, "MyCfnOIDCProvider",
    thumbprint_list=["6938fd4d98bab03faadb97b34396831e3780aea1"],
    client_id_list=["sts.amazonaws.com"],
    url="https://token.actions.githubusercontent.com"
)
```

The thumbprint above is unique to Github Actions. For the full detail on how it is obtained
for any OIDC provider check out this [AWS doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html).
We also use the url for the issuer of the OIDC token.

With that done we then need to create an IAM role which will be assumed in the Github Actions workflow.
In the role we specify an Assume Role Trust Policy which verifies the claim coming from Github Actions.
Here I am matching on a specific repository; as long as the workflow live in that repo the claim will
be verified successfully and temporary security credentials will be created allowing the workflow to assume the role.

```python
oidc_role = iam.Role(
            self, 
            'OIDCRole', 
            assumed_by=iam.WebIdentityPrincipal(
                cfn_oidc_provider.attr_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": "repo:theo-r/aws-oidc-provider:*",
                        }
                })
            )
```

Below is the code in it's entirety for our stack. The last touch included is to attach a policy
to our role granting read only access to the AWS account. This is purely for testing
purposes to make sure our set-up is working correctly. In practice we will need to
create a set of permissions which will match our use-case.


```python
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
)


class OIDCProviderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_oidc_provider = iam.CfnOIDCProvider(
            self, "MyCfnOIDCProvider",
            thumbprint_list=["6938fd4d98bab03faadb97b34396831e3780aea1"],
            client_id_list=["sts.amazonaws.com"],
            url="https://token.actions.githubusercontent.com"
        )

        oidc_role = iam.Role(
            self, 
            'OIDCRole', 
            assumed_by=iam.WebIdentityPrincipal(
                cfn_oidc_provider.attr_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": "repo:theo-r/aws-oidc-provider:*",
                        }
                })
            )
        
        oidc_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('ReadOnlyAccess'))
```

All that remains to do now is to create a workflow to prove that
the role in our AWS account can be assumed using the OIDC flow. The below workflow does just that.

```yaml
name: AWS Workflow
on:
  push
permissions:
  id-token: write
  contents: read
jobs:
  CheckAccess:
    runs-on: ubuntu-latest
    steps:
      - name: Git clone the repository
        uses: actions/checkout@v2
      - name: configure aws credentials
        uses: aws-actions/configure-aws-credentials@master
        with:
          role-to-assume: ${{ secrets.ROLE_ARN }}
          role-session-name: githubactions
          aws-region: eu-west-1
      - name:  Check permissions
        run: |
          aws s3 ls
```

Success! Our Github Actions workflow has access to our AWS resources with
no pesky long-lived access credentials lurking in the shadows.

The full source code can be found [here]](https://github.com/theo-r/aws-oidc-provider)
