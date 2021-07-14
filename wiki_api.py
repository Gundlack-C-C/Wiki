import requests

wiki_api = "https://en.wikipedia.org/api/rest_v1/"

def get_article_from_page(page):
    return {
        "text": {
            "title": page['title'], 
            "description": page['description'], 
            "short": page['extract']
        }, 
        "id": page['titles']['canonical'] 
    }

def get_wiki(title):
    S = requests.Session()
    URL = f"{wiki_api}page/summary/{title}"
    R = S.get(url=URL)
    page = R.json()
    return get_article_from_page(page)

def get_random_wiki():
    S = requests.Session()
    URL = f"{wiki_api}page/random/summary"
    R = S.get(url=URL)
    page = R.json()
    return get_article_from_page(page)


