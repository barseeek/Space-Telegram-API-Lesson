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
        save_photo(image_url, filename, params=params)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    get_nasa_epic_photos(nasa_api_key)


if __name__ == '__main__':
    main()
