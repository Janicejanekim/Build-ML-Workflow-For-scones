import json

THRESHOLD = 0.7

def lambda_handler(event, context):
    # Extract the 'body' from the event
    body = event.get('body', {})

    # Ensure 'inferences' is in the body
    if 'inferences' not in body:
        raise Exception("'inferences' not found in event body")

    inferences = body['inferences']

    # Check if any inference exceeds the threshold
    meets_threshold = any(float(inference) > THRESHOLD for inference in inferences)

    if meets_threshold:
        return {
            'statusCode': 200,
            'body': json.dumps(body)  # Return the body as JSON string
        }
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
