# Space Telegram API Lesson

This is a project that uses the APIs of space organizations (SpaceX and NASA) to save photos from space and publish it to the Telegram channel.

Repository contains several scripts:

#### fetch_spacex_images.py
Retrieves photos from the last SpaceX launch or by a specified identifier using the SpaceX API.
Startup script argument is the launch `id`. If `id` is empty, takes photo from latest launch.
Saves the images locally.
#### fetch_epic_images.py

Retrieve Earth photos from the EPIC camera. Retrieves photo data, generates URLs, and saves images locally based on date.

#### fetch_apod_images.py
Retrieve Photos of the Day in Astronomy.
Extracts the URL of the photos of the day, determines the file extension from the URL, and saves photos locally.

#### publish_photos_to_tgchannel.py
Publish photos from the ``images`` folder to the Telegram channel [Space Images](https://t.me/space_imagess) with the delay specified in the argument `timer` at startup.
If argument `timer` is empty, takes environment variable `PUBLISH_TIMER` (by default 4 hours).

#### publish_photo.py
Publishes the photo the Telegram channel [Space Images](https://t.me/space_imagess) by the name specified in the argument `filename` at startup. If argument is empty, publish random photo from folder. 

#### get_photo.py
A helper script with functions to save photo, get file name and file extension.


## How to install
1. Clone this repository or download the script to your local machine.

2. Create a `.env` file in the same directory as the script with the following content, filled in:
  * `NASA_API_KEY` - your actual [NASA access key](https://api.nasa.gov/):
  * `PUBLISH_TIMER` - publish delay time in seconds
  * `TELEGRAM_BOT_TOKEN` - your actual [BOT TOKEN](https://t.me/BotFather)
  * `TELEGRAM_CHAT_ID` - link to your telegram channel

```
NASA_API_KEY=YOUR_NASA_API_KEY
PUBLISH_TIMER=YOUR_TIMER_IN_SECONDS
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
```
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## How to run
Startup script argument is the launch `id`. If `id` is empty, takes photo from latest launch.
```
python fetch_spacex_images.py 5eb87d46ffd86e000604b388
python fetch_spacex_images.py
```
```
python fetch_epic_images.py
```
```
python fetch_apod_images.py
```
Startup script argument is the launch `timer`. If `timer` is empty, the default environment variable `PUBLISH_TIMER` value is 14400 seconds .
```
python publish_photos_to_tgchannel.py 1000
python publish_photos_to_tgchannel.py
```
Startup script argument is the launch `filename`. If `filename` is empty, publish random photo from image folder.
```
python publish_photo.py apod_2023-11-10.jpg
python publish_photo.py 
```
## Project Goals
The goal of the project is to automate the collection and storage of space photos provided by space agencies through their APIs. All scripts allow you to retrieve images and store them locally for further use or analysis.

*PS. The code is written for educational purposes on online-course for web-developers dvmn.org.*
