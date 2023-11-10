import requests
import os

from datetime import datetime
from dotenv import load_dotenv
from get_photo import save_photo


def get_nasa_epic_photos():
    load_dotenv()
    params = {
        'api_key': os.environ['NASA_API_KEY']
    }
    url = "https://api.nasa.gov/EPIC/api/natural"
    save_url = "https://api.nasa.gov/EPIC/archive/natural"
    response = requests.get(url, params=params)
    photos = response.json()
    for photo in photos:
        filename = "{0}.{1}".format(photo["image"], "png")
        date_string = datetime.fromisoformat(photo["date"]).date().strftime("%Y/%m/%d")
        image_url = "/".join([save_url, date_string, "png", filename ])
        response = requests.get(image_url,params=params)
        save_photo(response.url,filename)


def main():
    get_nasa_epic_photos()


if __name__ == '__main__':
    main()