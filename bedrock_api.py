from dotenv import load_dotenv
import os
import boto3
import json

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=aws_default_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

print("Bedrock client initialized successfully!")

payload = {
    "prompt": "What are the benefits of using AI in modern businesses?",
    "max_tokens_to_sample": 100,  # Number of tokens in the response
    "temperature": 0.7,           # Controls the creativity of the response
    "top_k": 50,                  # Token sampling range
    "top_p": 0.9                  # Nucleus sampling
}


try:
    response = bedrock.invoke_model_with_response_stream(
        modelId="anthropic.claude-v2",  # Need to put our model
        accept="application/json",
        contentType="application/json",
        body=json.dumps(payload)
    )

    response_body = b""
    for event in response["body"]:
        response_body += event["bytes"]
    response_data = json.loads(response_body.decode("utf-8"))

    print("Model Response:")
    print(response_data.get("completion", "No response received."))

except Exception as e:
    print("Error invoking the Bedrock model:", str(e))
