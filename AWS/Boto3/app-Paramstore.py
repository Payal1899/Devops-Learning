import boto3
from dotenv import load_dotenv
import os
load_dotenv()

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

# AWS PARAM STORE
ssm = boto3.client('ssm', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY, region_name='us-east-1')
# region name should be the one where param is created and not the one used for aws config profile
#this line created boto3 client of AWS service ssm, provided key id's and region for the resource, our resource i.e. parameter store is in us east region
#parameter store are regional

# Get a parameter from the parameter store
response = ssm.get_parameter(Name='firstParam', WithDecryption=True)

print(response['Parameter']['Value'])