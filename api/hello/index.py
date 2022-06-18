import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"{event=}")
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello, world!'})
    }
    return response