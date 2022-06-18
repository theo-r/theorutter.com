def lambda_handler(event, context):
    print(event)
    response = event["Records"][0]["cf"]["response"]
    request = event['Records'][0]['cf']['request']

    if "headers" not in response:
        response["headers"] = {}

    if "origin" in request["headers"]:
        response["headers"]["access-control-allow-origin"] = [
            {"Access-Control-Allow-Origin", "*"},
        ]
        response["headers"]["access-control-allow-methods"] = [
            {"Access-Control-Allow-Methods", "GET, HEAD, POST"}
        ]
        response["headers"]["access-control-max-age"] = [
            {"Access-Control-Max-Age": "86400"}
        ]
    
    return response