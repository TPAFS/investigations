import shutil
import urllib


def download_file_from_url(url: str, target_filepath: str) -> None:
    print(f"Downloading file from: {url}.")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response, open(
            target_filepath, "wb"
        ) as target_file:
            shutil.copyfileobj(response, target_file)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("We failed to reach a server.")
        print("Reason: ", e.reason)
    print("Success.")
    return None
