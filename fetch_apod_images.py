import requests
import os

from datetime import datetime
from dotenv import load_dotenv
from get_photo import save_photo
from get_photo import get_extension


def get_nasa_apod_photos():
    load_dotenv()
    params = {
        'api_key': os.environ['NASA_API_KEY']
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    photo_url = response.json()["url"]
    photo_ext = get_extension(photo_url)
    save_photo(
        photo_url,
        "apod_{0}{1}".format(
            datetime.date(datetime.now()),
            photo_ext
        )
    )


def main():
    get_nasa_apod_photos()


if __name__ == '__main__':
    main()