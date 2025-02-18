import requests
from .. import config
from termcolor import colored

def get_file_metadata():
    """
    Fetches metadata for the given ENCODE file accession.
    """
    url = f"{config.ENCODE_BASE_URL}files/{config.ENCODE_FILE_ACCESSION}/?frame=object"
    headers = {"accept": "application/json"}

    print(colored(f"🔍 Fetching metadata from {url}", "yellow"))

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(colored("✅ Metadata fetched successfully!", "green"))
        return response.json()
    else:
        print(colored(f"❌ Error {response.status_code}: Unable to fetch metadata", "red"))
        return None

def get_download_url(file_metadata):
    """
    Extracts the direct file download URL from the metadata.
    """
    if not file_metadata or 'href' not in file_metadata:
        print(colored("❌ No download URL found in metadata!", "red"))
        return None

    download_url = config.ENCODE_BASE_URL.rstrip('/') + file_metadata['href']
    print(colored(f"📥 File available at: {download_url}", "cyan"))
    return download_url

if __name__ == "__main__":
    metadata = get_file_metadata()
    if metadata:
        get_download_url(metadata)
