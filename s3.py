from handle_vocab_file import vocab, filename
import boto3

bucket_name = "vocabulary_trainer"
region_name = "us-west_2"

s3_client = boto3.client("s3", region=region_name)
