import requests
import argparse

from pathlib import Path
from get_photo import get_extension
from get_photo import save_photo


def fetch_spacex_last_launch(launch_id="latest"):
    path = Path("images/")
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    photo_links = response.json()["links"]["flickr"]["original"]
    for photo_number, photo_url in enumerate(photo_links):
        photo_ext = get_extension(photo_url)
        filename = "{0}_{1}{2}".format("spacex", photo_number, photo_ext)
        save_photo(photo_url, filename, path)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Get photos from spacex launch by id'
    )
    parser.add_argument(
        'id',
        nargs='?',
        help='Enter launch id',
        default='latest'
    )
    return parser


def main():
    parser = create_parser()
    arguments = parser.parse_args()
    fetch_spacex_last_launch(arguments.id)


if __name__ == '__main__':
    main()
