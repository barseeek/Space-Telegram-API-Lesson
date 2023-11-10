import telegram 
import os

from dotenv import load_dotenv

def main():
    load_dotenv()
    chat_id = "@space_imagess"
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    bot.send_photo(chat_id=chat_id, photo=open('images/apod_2023-11-10.jpg', 'rb'))

if __name__ == "__main__":
    main()