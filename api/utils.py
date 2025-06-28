import os
import boto3
from botocore.client import Config
from django.conf import settings

def get_spaces_client():
    """Return a boto3 client for DigitalOcean Spaces using environment variables."""
    session = boto3.session.Session()
    client = session.client(
        's3',
        region_name=os.environ.get('AWS_REGION', 'nyc3'),
        endpoint_url=os.environ.get('DO_SPACES_ENDPOINT', settings.AWS_S3_ENDPOINT_URL),
        aws_access_key_id=os.environ.get('DO_SPACES_KEY', settings.AWS_ACCESS_KEY_ID),
        aws_secret_access_key=os.environ.get('DO_SPACES_SECRET', settings.AWS_SECRET_ACCESS_KEY),
        config=Config(signature_version='s3v4')
    )
    return client

def upload_file_to_spaces(file_obj, object_name=None, bucket_name=None, acl='public-read'):
    """
    Upload a file-like object to DigitalOcean Spaces using boto3 and environment variables.
    Usage: upload_file_to_spaces(file_obj, 'uploads/file.jpg')
    """
    client = get_spaces_client()
    bucket = bucket_name or os.environ.get('DO_SPACES_BUCKET', settings.AWS_STORAGE_BUCKET_NAME)
    if object_name is None:
        object_name = getattr(file_obj, 'name', 'uploaded_file')
    object_name = os.path.basename(object_name)
    client.upload_fileobj(file_obj, bucket, object_name, ExtraArgs={'ACL': acl})
    base_url = os.environ.get('DO_SPACES_CDN', getattr(settings, 'AWS_S3_CUSTOM_DOMAIN', settings.AWS_S3_ENDPOINT_URL))
    url = f"{base_url}/{object_name}"
    return url
