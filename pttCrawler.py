import requests
from requests_html import HTML


def fetch(url):
    response = requests.get(url)
    return response


def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries


def parse_article_meta(entry):
    return {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text,
        'author': entry.find('div.author', first=True).text
    }


url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = fetch(url)
post_entries = parse_article_entries(resp.text)

for entry in post_entries:
    meta = parse_article_meta(entry)
    print(meta)