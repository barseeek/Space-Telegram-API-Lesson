import telegram 
import os

from dotenv import load_dotenv

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    bot.send_message(text="First message", chat_id="@space_imagess")

if __name__ == "__main__":
    main()