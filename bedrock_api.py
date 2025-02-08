import json
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
    service_name="bedrock-runtime",
    region_name=aws_default_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Define payload
payload = {
    "prompt": "Explain the benefits of AI in business.",
    "max_gen_len": 100,  # Number of tokens in the response
    "temperature": 0.7,  # Controls creativity
    "top_p": 0.9         # Nucleus sampling
}

try:
    # Meta Llama 3 70B model
    response = bedrock.invoke_model_with_response_stream(
        modelId="meta.llama3-70b-instruct-v1:0",  
        accept="application/json",
        contentType="application/json",
        body=json.dumps(payload)
    )

    accumulated_text = ""

    for event in response['body']:
        if 'chunk' in event and 'bytes' in event['chunk']:
            chunk_data = json.loads(event['chunk']['bytes'].decode('utf-8'))
            if 'generation' in chunk_data:
                accumulated_text += chunk_data['generation']
    print("Model Response:")
    print(accumulated_text.strip())

except Exception as e:
    print("Error invoking the Bedrock model:", str(e))
