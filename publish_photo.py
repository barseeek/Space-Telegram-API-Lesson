import telegram
import os
import argparse
import random

from pathlib import Path
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description='Publish photos to @space_imagess'
    )
    parser.add_argument(
        'filename',
        nargs='?',
        help='Enter filename'
    )
    return parser


def main():
    load_dotenv()
    filename = create_parser().parse_args().filename
    if filename is None:
        photos = [photo for _, _, files in os.walk('images/')
                  for photo in files]
        filename = random.choice(photos)
    print(filename)
    chat_id = "@space_imagess"
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    bot.send_photo(
        chat_id=chat_id,
        photo=open(
            Path.joinpath(Path('images/'), Path(filename)),
            'rb'
        )
    )


if __name__ == "__main__":
    main()
