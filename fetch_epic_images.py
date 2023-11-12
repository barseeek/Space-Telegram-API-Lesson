from urllib.parse import urlparse, urlunparse
import requests
import os

from datetime import datetime
from dotenv import load_dotenv
from get_photo import save_photo


def get_nasa_epic_photos(api_key):
    params = {
        'api_key': api_key
    }
    url = "https://api.nasa.gov/EPIC/api/natural"
    url_to_download = "https://api.nasa.gov/EPIC/archive/natural"
    response = requests.get(url, params=params)
    photos = response.json()
    for photo in photos:
        filename = "{0}.{1}".format(photo["image"], "png")
        date_string = datetime.fromisoformat(photo["date"]) \
            .date().strftime("%Y/%m/%d")
        image_url = "/".join([url_to_download, date_string, "png", filename])
        parts_of_url = urlparse(image_url)._replace(query=f'api_key={api_key}')
        save_photo(urlunparse(parts_of_url), filename)


def main():
    api_key = os.environ['NASA_API_KEY']
    load_dotenv()
    get_nasa_epic_photos(api_key)


if __name__ == '__main__':
    main()
