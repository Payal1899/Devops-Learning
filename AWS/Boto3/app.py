import boto3

# Create an S3 resource
s3 = boto3.resource('s3')
#get all buckets
for bucket in s3.buckets.all():
    print(bucket.name)

'''
BUCKET_NAME = 'course-test-tutedude-3'
# Create a new bucket
s3.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

# delete bucket
s3.Bucket(BUCKET_NAME).delete()

# Read a file from the bucket
s3.Bucket(BUCKET_NAME).download_file('dotfiles/nvim/init.vim','test.txt')

first is public url path only folder portion from aws, second one i.e. test.txt is filename u want to store on your local machine

#Defining creds in code
import boto3

ACCESS_KEY_ID = 'AKIAZY65GL3LEKJZZWFD'
SECRET_ACCESS_KEY = 'J46K3V0JkuC8VCmE2V36YgtcjzZknVjlB3Iwk+SQ'

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY
)

# get all buckets
for bucket in s3.buckets.all():
    print(bucket.name)


#Defining .env for creds in code
import boto3

from dotenv import load_dotenv
import os
load_dotenv()
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY
)

# get all buckets
for bucket in s3.buckets.all():
    print(bucket.name)
'''    
