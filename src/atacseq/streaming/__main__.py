from .encode_fetch import get_file_metadata, get_download_url
from .s3_upload import stream_to_s3
from .. import config  # Import from src/

import argparse 
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description="ATAC-Seq Data Streaming Pipeline")
    parser.add_argument("-a", "--accession", type=str, help="ENCODE File Accession Number", required=True)
    args = parser.parse_args()

    # Update config with user input
    config.ENCODE_FILE_ACCESSION = args.accession

    print(colored(f"🚀 Streaming ENCODE file: {config.ENCODE_FILE_ACCESSION}", "magenta"))

    metadata = get_file_metadata()
    if metadata:
        download_url = get_download_url(metadata)
        if download_url:
            s3_key = f"data/{config.ENCODE_FILE_ACCESSION}.fastq.gz"
            stream_to_s3(download_url, s3_key)

    print(colored("✅ Pipeline Complete!", "green"))

if __name__ == "__main__":
    main()
    # run-streaming -a ENCFF123ABC
