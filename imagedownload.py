import wget, shutil, os, bs4
from bs4 import BeautifulSoup
import requests
import configparser
import tweepy

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

darshan_tweets = api.home_timeline(screen_name="ISKCONPune", count=10,
                                   tweet_mode="extended")

media_files = set()

for status in darshan_tweets:
    media = status.entities.get('media', [])
    if len(media > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    file_name = wget.download(media_file)
    print("download successful %s", file_name)

    dest_folder = "D:\pythonD\\"
    shutil.copy(file_name, dest_folder + ".png")
    os.remove(file_name)






"""
headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


def download(link):
   name = image.get('alt')
   if name:
      if len(name) > 200:
         name = (image.get('alt')[0:20])
   else:
      return
   print(link)
   file_name = wget.download(link)
   print("download successful %s", file_name)

   dest_folder = "D:\pythonD\\"
   shutil.copy(file_name, dest_folder +name + ".png")
   os.remove(file_name)


url = input("Page URL:")
r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.content, 'html.parser')

images = bs.find_all("img")

count = 0
for image in images:
   link = image.get('src')

   if link and "http" in link:
      print(link)
      download(link)
      
      
"""



