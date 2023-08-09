import os
import requests
import shutil
import ssl
import urllib3


def download_file_from_url(
    url: str, target_filepath: str, legacy_ssl: bool = False
) -> None:
    if os.path.exists(target_filepath):
        print(f"Target file {target_filepath} already exists.")
        return None

    # Set legacy ssl context if desired, to allow DL from certain gov sites
    session = requests.session()
    if legacy_ssl:
        session = get_legacy_session()

    print(f"Downloading file from: {url}.")
    try:
        with session.get(url, stream=True) as response, open(
            target_filepath, "wb"
        ) as target_file:
            shutil.copyfileobj(response.raw, target_file)
        print("Success.")
    except requests.HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code: ", e.code)
    except requests.ConnectionError as e:
        print("We failed to reach a server.")
        print("Reason: ", e.reason)
    return None


class CustomHttpAdapter(requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=self.ssl_context,
        )


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount("https://", CustomHttpAdapter(ctx))
    return session
