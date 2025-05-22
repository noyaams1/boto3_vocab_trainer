import boto3

bucket_name = "vocab-trainer"
filename = "vocab_hebrew.json"
region = "us-west-2"
s3_client = boto3.client("s3", region_name=region)

def upload_vocab_to_s3(bucket_name, filename):
    try:
        s3_client = boto3.client("s3", region_name=region)
        s3_client.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
        )
        s3_client.upload_file(Filename=filename, Bucket=bucket_name, Key=filename)
        return True
    except Exception as e:
        print(f"Failed to upload to s3: {e}")
        return False


def download_vocab_file(bucket_name, filename, download_path):
    try:
        s3_client = boto3.client("s3", region_name=region)
        s3_client.download_file(bucket_name, filename, filename)
        return True
    except Exception as e:
        print(f"Failed to download from s3: {e}")
        return False


def enable_versioning(bucket_name):
    try:
        s3 = boto3.client("s3", region_name=region)
        s3.put_bucket_versioning(
            Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"}
        )
        print(f"Versioning enabled on bucket {bucket_name}")
        return True
    except Exception as e:
        print(f"Failed to enable versioning: {e}")
        return False

