import os
import boto3

def get_local_client():
    region_name = os.getenv("AWS_REGION")
    dynamodb = boto3.client("dynamodb", endpoint_url='http://localhost:8000', region_name=region_name)
    return dynamodb