from aws_cdk import (
    CfnOutput, Stack, 
    aws_lambda as _lambda, 
    aws_dynamodb as dynamodb
)
import aws_cdk.aws_apigatewayv2_alpha as apigwv2
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration


class ApiStack(Stack):
    def __init__(self, scope, construct_id, props, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        hit_counter_table = dynamodb.Table(
            self, "HitCounterTable",
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            partition_key=dynamodb.Attribute(
                name="slug",
                type=dynamodb.AttributeType.STRING
            )
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

        default_integration = HttpLambdaIntegration(
            "DefaultIntegration",
            default_lambda
        )

        hit_counter_integration = HttpLambdaIntegration(
            "HitCounterIntegration",
            hit_counter_lambda
        )

        self.http_api = apigwv2.HttpApi(self, "HttpApi")

        self.http_api.add_routes(
            path="/api",
            methods=[apigwv2.HttpMethod.GET],
            integration=default_integration
        )

        self.http_api.add_routes(
            path="/api/hit_counter",
            methods=[apigwv2.HttpMethod.GET],
            integration=hit_counter_integration
        )

        hit_counter_table.grant_read_write_data(hit_counter_lambda)