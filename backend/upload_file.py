import boto3

s3 = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Загрузка
s3.upload_file('example.txt', 'lab-bucket', 'example.txt')
# Скачивание
s3.download_file('lab-bucket', 'example.txt', 'example_downloaded.txt')