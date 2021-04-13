from bs4 import BeautifulSoup
import requests


def get_name_songs(date: str) -> list:
    res = requests.get(f'https://www.billboard.com/charts/hot-100/{date}').text
    soup = BeautifulSoup(res, 'html.parser')
    song_names_raw = soup.find_all(
        'span', class_='chart-element__information__song text--truncate color--primary'
    )
    return [i.string for i in song_names_raw]
