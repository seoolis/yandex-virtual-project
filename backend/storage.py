import os
import boto3
from botocore.client import Config

BUCKET_NAME = "malysheva-bucket"
ENDPOINT_URL = "https://storage.yandexcloud.net"
ACCESS_KEY = os.getenv("YC_ACCESS_KEY")
SECRET_KEY = os.getenv("YC_SECRET_KEY")

s3 = boto3.client(
    's3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4')
)


def upload_file(file_name, object_name=None):
    """Загрузка файла в бакет"""
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, BUCKET_NAME, object_name)
    return f"{ENDPOINT_URL}/{BUCKET_NAME}/{object_name}"

def get_file_url(object_name):
    """Получение публичного URL файла"""
    return f"{ENDPOINT_URL}/{BUCKET_NAME}/{object_name}"