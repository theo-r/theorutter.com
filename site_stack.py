from aws_cdk import CfnOutput, Stack, aws_lambda as _lambda
from static_site import StaticSitePublicS3
import aws_cdk.aws_apigatewayv2_alpha as apigwv2
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration


class StaticSiteStack(Stack):
    def __init__(self, scope, construct_id, props, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        site_domain_name = props["domain_name"]
        if props["sub_domain_name"]:
            site_domain_name = (
                f'{props["sub_domain_name"]}.{props["domain_name"]}'
            )

        site = StaticSitePublicS3(
            self,
            f"{props['namespace']}-construct",
            site_domain_name=site_domain_name,
            domain_certificate_arn=props["domain_certificate_arn"],
            origin_referer_header_parameter_name=props[
                "origin_custom_header_parameter_name"
            ],
            hosted_zone_id=props["hosted_zone_id"],
            hosted_zone_name=props["hosted_zone_name"],
        )

        test_lambda = _lambda.Function(self, "TestLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="test_lambda.lambda_handler",
            code=_lambda.Code.from_asset(path="test-lambda")
        )

        user_query_integration = HttpLambdaIntegration(
            "TestIntegration", 
            test_lambda
        )

        http_api = apigwv2.HttpApi(self, "HttpApi")

        http_api.add_routes(
            path="/get_tracks_data",
            methods=[apigwv2.HttpMethod.GET],
            integration=user_query_integration
        )

        CfnOutput(
            self,
            "HttpApiEndpoint",
            value=http_api.api_endpoint
        )
        CfnOutput(
            self,
            "HttpApiId",
            value=http_api.api_id
        )
        CfnOutput(
            self,
            "SiteBucketName",
            value=site.bucket.bucket_name,
        )
        CfnOutput(
            self,
            "DistributionId",
            value=site.distribution.distribution_id,
        )
        CfnOutput(
            self,
            "CertificateArn",
            value=site.certificate.certificate_arn,
        )