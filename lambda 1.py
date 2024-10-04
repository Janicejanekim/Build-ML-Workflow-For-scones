import json
import base64
import sagemaker
from sagemaker.serializers import IdentitySerializer

ENDPOINT = 'image-classification-2024-09-13-14-16-34-029'

def lambda_handler(event, context):
    # Extract the 'body' from the event
    body = event.get('body', {})
    
    # Ensure 'image_data' is in the body
    if 'image_data' not in body:
        raise Exception("'image_data' not found in event body")

    # Decode the base64 image
    image_data = body['image_data']
    image = base64.b64decode(image_data)

    # Set up the predictor
    predictor = sagemaker.predictor.Predictor(ENDPOINT)
    predictor.serializer = IdentitySerializer("image/png")

    # Get prediction
    inferences = predictor.predict(image)

    # Add inferences to the body
    body['inferences'] = json.loads(inferences.decode('utf-8'))

    return {
        'statusCode': 200,
        'body': body  # Return the body directly as dict
    }
