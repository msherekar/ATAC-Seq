import requests
import boto3
from .. import config 
from termcolor import colored
from .encode_fetch import get_file_metadata, get_download_url

# Initialize S3 Client
s3_client = boto3.client("s3")

def stream_to_s3(download_url, s3_key):
    """
    Streams an ENCODE file directly into an S3 bucket without saving it locally.
    """
    print(colored(f"🚀 Streaming file from {download_url} → Uploading to S3: {config.S3_BUCKET}/{s3_key}", "yellow"))

    with requests.get(download_url, stream=True) as response:
        if response.status_code == 200:
            s3_client.upload_fileobj(response.raw, config.S3_BUCKET, s3_key)
            print(colored(f"✅ Successfully uploaded to s3://{config.S3_BUCKET}/{s3_key}", "green"))
        else:
            print(colored(f"❌ Error {response.status_code}: Unable to download file.", "red"))

if __name__ == "__main__":
    metadata = get_file_metadata()
    if metadata:
        download_url = get_download_url(metadata)
        if download_url:
            s3_key = f"data/{config.ENCODE_FILE_ACCESSION}.fastq.gz"
            stream_to_s3(download_url, s3_key)
