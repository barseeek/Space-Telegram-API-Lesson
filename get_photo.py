import requests
import os

from urllib.parse import urlparse
from pathlib import Path


def save_photo(url, filename, path=Path("images/"), params={}):
    filepath = Path("{0}/{1}".format(path, filename))
    path.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    hierarchical_path = urlparse(url).path
    extension = os.path.splitext(hierarchical_path)[1]
    return extension
