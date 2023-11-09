import requests
import os
import datetime

from urllib.parse import urlparse
from pathlib import Path
from dotenv import load_dotenv


def save_photo(url,filename, path=Path("images/")):
    filepath = Path("{0}/{1}".format(path, filename))
    path.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url,path):
    response = requests.get(url)
    response.raise_for_status()
    photo_links = response.json()["links"]["flickr"]["original"]
    for photo_number, photo_url in enumerate(photo_links):
        photo_ext = get_extension(photo_url)
        filename = get_filename("spacex", photo_number, photo_ext)
        save_photo(photo_url, filename, path)    


def get_filename(prefix, number, extension):
    return "{0}_{1}{2}".format(prefix, number, extension)


def get_extension(url):
    hierarchical_path = urlparse(url).path
    extension = os.path.splitext(hierarchical_path)[1]
    return extension


def get_nasa_photos():
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
        date_string = datetime.datetime.fromisoformat(photo["date"]).date().strftime("%Y/%m/%d")
        image_url = "/".join([save_url, date_string, "png", filename ])
        response = requests.get(image_url,params=params)
        print(response.url)
        save_photo(response.url,filename)
    


def main():
    path = Path('images/')
    id = "5eb87d47ffd86e000604b38a"
    url_spacex = f"https://api.spacexdata.com/v5/launches/{id}"
    fetch_spacex_last_launch(url_spacex, path)
    get_nasa_photos()


if __name__ == '__main__':
    main()
