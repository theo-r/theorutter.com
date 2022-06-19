import boto3
import os
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ddb = boto3.resource('dynamodb')
counter_table_name = os.getenv('COUNTER_TABLE_NAME')
counter_table = ddb.Table(counter_table_name)

def lambda_handler(event, context):
    logger.info(event)
    slug = event["queryStringParameters"]["slug"]
    logger.info(f"Slug: {slug}")
    res = counter_table.get_item(Key={"slug": slug})

    if 'Item' in res:
        logger.info(f"Hits: {res['Item']['hits']}. Updating...")
        new_hits = int(res['Item']['hits']) + 1
        response = counter_table.update_item(
            Key={"slug": slug}, 
            UpdateExpression='SET hits = :val1', 
            ExpressionAttributeValues={':val1': new_hits}
        )
    else:
        logger.info("Item not found: creating a new item")
        new_hits = 1
        response = counter_table.put_item(Item={"slug": slug, "hits": 1}) 

    response = {
        'statusCode': 200,
        'body': json.dumps({'hits': new_hits})
    }
    return response