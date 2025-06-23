import json
import boto3
import os
import base64
from botocore.exceptions import ClientError

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response['SecretString'])
    except ClientError as e:
        print(f"Secret error: {e}")
        raise

def call_bedrock(prompt):
    # Replace this with real Bedrock call
    return {"provider": "bedrock", "response": f"Bedrock response for '{prompt}'"}

def call_azure(prompt, azure_key):
    # Placeholder for Azure OpenAI call
    return {"provider": "azure", "response": f"(Simulated) Azure response for '{prompt}'"}

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    prompt = body.get('prompt')
    model = body.get('target_model')

    secrets = get_secret(os.environ['SECRET_NAME'])

    if model == "bedrock":
        response = call_bedrock(prompt)
    elif model == "azure":
        response = call_azure(prompt, secrets.get('azure_api_key'))
    else:
        return {"statusCode": 400, "body": json.dumps({"error": "Invalid target_model"})}

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
