import telegram 
import os

from dotenv import load_dotenv

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    print(bot.get_me())

if __name__ == "__main__":
    main()