from bs4 import BeautifulSoup
import requests
import src.config as config


def FindLinksFromWiki(link):
    main_link = f'https://{config.LANGUAGE}.wikipedia.org'
    soup = BeautifulSoup(requests.get(url=link).content, 'html.parser')
    title = soup.find(id="firstHeading").text
    all_links = set()
    for i in soup.find(id="bodyContent").find_all("a"):
        if not i.has_attr('href'):
            continue
        elif i['href'].find('/wiki/') == -1:
            continue
        elif i['href'].find('(') != -1:
            continue
        elif i['href'].find(':') != -1:
            continue
        all_links = all_links.union({main_link + i['href']})
    return title, all_links
