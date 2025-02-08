from dotenv import load_dotenv
import os
import boto3

# Load AWS credentials
load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# Initialize Bedrock client
bedrock = boto3.client(
    service_name="bedrock",
    region_name=aws_default_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# List models
try:
    response = bedrock.list_foundation_models()
    print("Available models:")
    for model in response.get("modelSummaries", []):  # Access the correct key
        print(f"Model Name: {model['modelName']}")
        print(f"Model ID: {model['modelId']}")
        print(f"Provider: {model['providerName']}")
        print(f"Input Modalities: {', '.join(model['inputModalities'])}")
        print(f"Output Modalities: {', '.join(model['outputModalities'])}")
        print(f"Supported Inference Types: {', '.join(model['inferenceTypesSupported'])}")
        print("-" * 50)
except Exception as e:
    print("Error listing models:", str(e))
