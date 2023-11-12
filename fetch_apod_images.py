import requests
import os

from dotenv import load_dotenv
from get_photo import save_photo
from get_photo import get_extension


def get_nasa_apod_photos(api_key):
    params = {
        'api_key': api_key,
        'count': 30
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    photos = response.json()
    for photo_number, photo in enumerate(photos):
        photo_url = photo["url"]
        photo_ext = get_extension(photo_url)
        save_photo(
            photo_url,
            "nasa_apod_{0}{1}".format(
                photo_number,
                photo_ext
            )
        )


def main():
    api_key = os.environ['NASA_API_KEY']
    load_dotenv()
    get_nasa_apod_photos(api_key)


if __name__ == '__main__':
    main()
