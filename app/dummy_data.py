import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from database import engine
from models import Ad

URL = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"

def scrape_data():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    ads = []

    for position, ad in enumerate(soup.select('.bull-list-item-js -exact'), 1):
        title = ad.select_one('.bulletinLink bull-item__self-link auto-shy').text.strip()
        author = 'blank'
        views = int(ad.select_one('.views nano-eye-text').text.strip())

        ads.append({
            'title': title,
            'author': author,
            'views': views,
            'position': position
        })
    
    return ads

def populate_database():
    ads = scrape_data()
    session = Session(bind=engine)
    for ad in ads:
        advert = Ad(**ad)
        session.add(advert)
    session.commit()
    session.close()

if __name__ == '__main__':
    populate_database()