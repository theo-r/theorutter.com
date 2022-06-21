from aws_cdk import (
    CfnOutput, Stack, 
    aws_lambda as _lambda, 
    aws_cloudfront as cloudfront, 
    aws_dynamodb as dynamodb
)
from static_site import StaticSitePublicS3ApiGateway
import aws_cdk.aws_apigatewayv2_alpha as apigwv2
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration


class StaticSiteStack(Stack):
    def __init__(self, scope, construct_id, props, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # create dynamo table
        hit_counter_table = dynamodb.Table(
            self, "HitCounterTable",
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            partition_key=dynamodb.Attribute(
                name="slug",
                type=dynamodb.AttributeType.STRING
            )
        )

        hello_lambda = _lambda.Function(self, "HelloLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset(path="api/hello")
        )

        default_lambda = _lambda.Function(self, "DefaultLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset(path="api/default")
        )

        hit_counter_lambda = _lambda.Function(self, "HitCounterLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset(path="api/hit_counter")
            )
        hit_counter_lambda.add_environment("COUNTER_TABLE_NAME", hit_counter_table.table_name)

        hello_integration = HttpLambdaIntegration(
            "hello_integration", 
            hello_lambda
        )

        default_integration = HttpLambdaIntegration(
            "DefaultIntegration",
            default_lambda
        )

        hit_counter_integration = HttpLambdaIntegration(
            "HitCounterIntegration",
            hit_counter_lambda
        )

        http_api = apigwv2.HttpApi(self, "HttpApi")

        http_api.add_routes(
            path="/api",
            methods=[apigwv2.HttpMethod.GET],
            integration=default_integration
        )

        http_api.add_routes(
            path="/api/hello",
            methods=[apigwv2.HttpMethod.GET],
            integration=hello_integration
        )

        http_api.add_routes(
            path="/api/hit_counter",
            methods=[apigwv2.HttpMethod.GET],
            integration=hit_counter_integration
        )

        hit_counter_table.grant_read_write_data(hit_counter_lambda)

        site_domain_name = props["domain_name"]
        if props["sub_domain_name"]:
            site_domain_name = (
                f'{props["sub_domain_name"]}.{props["domain_name"]}'
            )

        site = StaticSitePublicS3ApiGateway(
            self,
            f"{props['namespace']}-construct",
            site_domain_name=site_domain_name,
            domain_certificate_arn=props["domain_certificate_arn"],
            origin_referer_header_parameter_name=props[
                "origin_custom_header_parameter_name"
            ],
            hosted_zone_id=props["hosted_zone_id"],
            hosted_zone_name=props["hosted_zone_name"],
            apigw_domain_name=f"{http_api.api_id}.execute-api.{self.region}.amazonaws.com",
        )

        CfnOutput(
            self,
            "HttpApiEndpoint",
            value=http_api.api_endpoint,
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