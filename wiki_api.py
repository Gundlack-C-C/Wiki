import requests

wiki_api = "https://en.wikipedia.org/api/rest_v1/"

def get_wiki(title):
    S = requests.Session()
    URL = f"{wiki_api}page/summary/{title}"
    R = S.get(url=URL)
    page = R.json()

    return f"{page['title']}. {page['extract']}"

def get_random_wiki():
    S = requests.Session()
    URL = f"{wiki_api}page/random/summary"
    R = S.get(url=URL)
    page = R.json()

    return f"{page['title']}. {page['extract']}"