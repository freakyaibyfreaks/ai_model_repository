import boto3
import botocore
import sys
import os
# Unzip downloaded file from S3
import zipfile

# Adding parent's path
sys.path.append('../')

# IAM user credentials
from credentials import access_key_id, secret_access_key
 
session = boto3.Session(
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
)

BUCKET_NAME = 'data-handwritten-model' # replace with your bucket name
KEY = 'saintgalldb.zip' # replace with your object key

s3 = session.resource('s3')


class DownloadData():
    """ Constructor """
    def __init__(self):
        pass

    def get_file(self, BUCKET_NAME, KEY):
        try:
            s3.Bucket(BUCKET_NAME).download_file(KEY, KEY)
            print('File downloaded successfully')

        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def unzip_file(self, fileName):
        try:
            with zipfile.ZipFile(fileName, 'r') as zip_ref:
                zip_ref.extractall('')

        except Exception as e:
            print(e)   


