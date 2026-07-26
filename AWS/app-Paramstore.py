import boto3
from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
print(ACCESS_KEY_ID)
# AWS PARAM STORE

ssm = boto3.client('ssm', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

# Get a parameter from the parameter store

response = ssm.get_parameter(Name='firstParam', WithDecryption=True)

print(response['Parameter']['Value'])