from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


date = '2021-04-10'  # input('Enter date to scratch YYYY-MM-DD: ')

res = requests.get(f'https://www.billboard.com/charts/hot-100/{date}').text

soup = BeautifulSoup(res, 'html.parser')

song_names_raw = soup.find_all(
    'span', class_='chart-element__information__song text--truncate color--primary'
)

song_names = [i.string for i in song_names_raw]
print(song_names)
