import random
import argparse
import os
import telegram

from time import sleep
from dotenv import load_dotenv
from pathlib import Path


def create_parser(timer):
    parser = argparse.ArgumentParser(
        description='Publish photos to tg channel'
    )
    parser.add_argument(
        'timer',
        nargs='?',
        help='Enter publishing delay in sec',
        default=timer,
        type=int
    )
    return parser


def publish_photo_with_timer(bot, TELEGRAM_CHAT_ID, timer, path):
    photos = [photo for _, _, files in os.walk(path) for photo in files]
    while True:
        for photo in photos:
            with open(
                Path.joinpath(path, Path(photo)),
                'rb'
            ) as photo_file:
                bot.send_photo(
                    TELEGRAM_CHAT_ID=TELEGRAM_CHAT_ID,
                    photo=photo_file
                    )
                sleep(timer)
        random.shuffle(photos)


def main():
    load_dotenv()
    default_timer = os.environ['PUBLISH_TIMER']
    arguments = create_parser(default_timer).parse_args()
    TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    path = Path('images/')
    publish_photo_with_timer(bot, TELEGRAM_CHAT_ID, arguments.timer, path)


if __name__ == '__main__':
    main()
