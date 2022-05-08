import boto3
import json
secret_keys = "secret_keys.json"
with open(secret_keys, 'r') as f:
     keys = json.loads(f.read())
aws_access_key_id = keys["aws_access_key_id"]
aws_secret_access_key = keys["aws_secret_access_key"] 
s3 = boto3.client('s3',aws_access_key_id=aws_access_key_id ,aws_secret_access_key=aws_secret_access_key )


def download_cv():
    file = s3.get_object(Bucket="cv-elyasaf-lehrer", Key='CV-Elyasaf-Lehrer.pdf')
    return file



