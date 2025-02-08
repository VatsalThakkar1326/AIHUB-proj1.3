#Blue Sky

Steps to Run Locally
Clone the repository:

git clone <repository_url>
cd <repository_name>
Set up a virtual environment:

python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory with the following:
AWS_ACCESS_KEY_ID=<your_access_key>
AWS_SECRET_ACCESS_KEY=<your_secret_key>
AWS_REGION=<your_region>

Run the script:
python bedrock_api.py
