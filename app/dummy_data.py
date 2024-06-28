import chardet
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.db import engine
from app.models import Ad

HTML_FILE = "source.html"

def scrape_data():
    with open(HTML_FILE, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        content = raw_data.decode(encoding)

    soup = BeautifulSoup(content, 'html.parser')

    ads = []
    for ad_element in soup.select("tr.bull-list-item-js"):  
        title_element = ad_element.select_one(".bull-item__self-link")
        views_element = ad_element.select_one(".views")
        position_attribute = ad_element.get("data-doc-id")
        author_element = ad_element.select_one(".address")

        if title_element and author_element and views_element and position_attribute:
            title = title_element.text.strip()
            author = author_element.text.strip()
            views = int(views_element.text.strip())
            position = int(position_attribute)

            ads.append({
                "title": title,
                "author": author,
                "views": views,
                "position": position
            })
    print(*ads, sep='\n')
    return ads

def populate_db():
    ads = scrape_data()
    session = Session(bind=engine)
    for ad in ads:
        advertisement = Ad(**ad)
        session.add(advertisement)
    session.commit()
    session.close()

if __name__ == "__main__":
    populate_db()