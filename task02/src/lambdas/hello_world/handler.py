import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def handle_request(self, event, context):
        
        _LOG.info(f"Event: {event}")

        http_method = event["requestContext"]["http"]["method"]
        path = event["requestContext"]["http"]["path"]

        if http_method == "GET" and path == "/hello":
           return {
               "statusCode": 200,
               "body": json.dumps({
                   "statusCode": 200,
                   "message": "Hello from Lambda"
               })
           }
        elif http_method == "GET" and path == "/cmtr-bc403d86":
           return {
               "statusCode": 200,
               "body": json.dumps({
                   "statusCode": 400,
                   "message": "Bad request syntax or unsupported method. Request path: {path}. HTTP method: {http_method}"})
             }
            
HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
