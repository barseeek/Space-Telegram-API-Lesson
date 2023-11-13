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
    if not (filename):
        photos = [photo for _, _, files in os.walk('images/')
                  for photo in files]
        filename = random.choice(photos)
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    with open(
        Path.joinpath(Path('images/'), Path(filename)),
        'rb'
    ) as photo_file:
        bot.send_photo(
            chat_id=telegram_chat_id,
            photo=photo_file
        )


if __name__ == "__main__":
    main()
