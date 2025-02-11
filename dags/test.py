import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://127.0.0.1:9000",
    aws_access_key_id="ROOTNAME",
    aws_secret_access_key="CHANGEME123"
)

response = s3.list_objects_v2(Bucket="airflow")
print(response)
