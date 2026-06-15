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
'''    
