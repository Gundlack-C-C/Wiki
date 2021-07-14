import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from itertools import chain
wiki_api = "https://en.wikipedia.org/api/rest_v1/"

def get_article_from_page(page):
    return {
        "text": {
            "title": page['title'], 
            "description": page['description'], 
            "short": page['extract']
        }, 
        "id": page['titles']['canonical'],
        "keywords": get_keywords(page['titles']['canonical'])
    }

def get_keywords(title, all=False):
    S = requests.Session()
    URL = f"{wiki_api}page/html/{title}"
    R = S.get(url=URL)
    S.close()
    
    parsed_html = BeautifulSoup(R.text, 'html.parser')
    # Remove Unwanted Content e.g. 
    for s in chain(*[parsed_html.select(f'table.{cls}') for cls in ['infobox', 'ambox', 'navbox-inner'] ]):
        s.extract()

    # Get Links
    links = []
    if not all:
        sections = parsed_html.body.find_all('section')
        links = sections[0].find_all('a', attrs={'rel': 'mw:WikiLink'})
    else:
        links = parsed_html.body.find_all('a', attrs={'rel': 'mw:WikiLink'})

    # Filter System links e.g. edit, add categories
    links = [a for a in links if 'Wikipedia:' not in a.get('href')]

    keywords = list(set([a.text for a in links]))
    return keywords

def get_wiki(title):
    S = requests.Session()
    URL = f"{wiki_api}page/summary/{title}"
    R = S.get(url=URL)
    page = R.json()
    S.close()
    return get_article_from_page(page)

def get_random_wiki():
    S = requests.Session()
    URL = f"{wiki_api}page/random/summary"
    R = S.get(url=URL)
    page = R.json()
    S.close()
    return get_article_from_page(page)


if __name__ == '__main__':
    # Example: Random Article - Summary
    print("######")
    print("Get random article from Wikipedia.en ...")
    article = get_random_wiki()
    print(article)
    print("######")

    # Example: Hello World Article - Summary
    print()
    print("######")
    print("Get article from Wikipedia.en by Title ['""Hello,_World!""_program'] ...")
    article = get_wiki('"Hello,_World!"_program')
    print(article)
    print("######")

     # Example: Hello World Article - Wikitext
    print()
    print("######")
    print("Get keywords from Wikipedia.en by Title ['Hamilton_Wright'] ...")
    article = get_keywords('Hamilton_Wright')
    print(article)
    print("######")