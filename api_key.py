from dotenv import load_dotenv
import os
from cohere import ClientV2
import time

### Load environment variables from .env file
load_dotenv()

### Access your API key
cohere_api_key = os.getenv('COHERE_API_KEY')

if not cohere_api_key:
    raise ValueError(
        "COHERE_API_KEY not found. Please create a .env file with your API key.\n"
        "See https://dashboard.cohere.com for instructions on getting your key."
    )

### Initialize the Cohere client using the V2 API
co = ClientV2(api_key=cohere_api_key)
print("API key loaded successfully from environment")