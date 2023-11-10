import random
import argparse
import os
import telegram

from time import sleep
from dotenv import load_dotenv
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser(
        description='Publish photos to @space_imagess'
    )
    parser.add_argument(
        'timer',
        nargs='?',
        help='Enter publishing delay in sec',
        default=os.environ['PUBLISH_TIMER'],
        type=int
    )
    return parser


def publish_photo_with_timer(bot, chat_id, timer, path):
    photos = [photo for _, _, files in os.walk(path) for photo in files]
    while True:
        for photo in photos:
            bot.send_photo(
                chat_id=chat_id,
                photo=open(
                    Path.joinpath(path, Path(photo)),
                    'rb'
                    )
                )
            sleep(timer)
        random.shuffle(photos)


def main():
    load_dotenv()
    arguments = create_parser().parse_args()
    chat_id = '@space_imagess'
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    path = Path('images/')
    publish_photo_with_timer(bot, chat_id, arguments.timer, path)


if __name__ == '__main__':
    main()
    