import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"{event=}")
    response = {
        'statusCode': 404,
        'body': json.dumps({'statusCode': '404', 'msg': 'Not found'})
    }
    return response