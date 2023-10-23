import os
import io
import boto3
import json
import base64
#from sagemaker.serializers import IdentitySerializer


# setting the  environment variables
ENDPOINT_NAME = 'image-classification-2023-10-23-18-34-20-341'
# # We will be using the AWS's lightweight runtime solution to invoke an endpoint.
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])
    
    # Make a prediction:
    predictor = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                    #   ContentType='image/png',
                                    ContentType='application/x-image',
                                      Body=image)
    
    # We return the data back to the Step Function    
    event["inferences"] = json.loads(predictor['Body'].read().decode('utf-8'))
    return {
        'statusCode': 200,
        # 'body': json.dumps(event)
        "body": {
            "image_data": event["body"]['image_data'],
            "s3_bucket": event["body"]['s3_bucket'],
            "s3_key": event["body"]['s3_key'],
            "inferences": event['inferences'],
       }
    }


