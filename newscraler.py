import requests
from bs4 import BeautifulSoup


#  -H 'X-Requested-With: XMLHttpRequest'"
def crawl():
    f = requests.get('http://www.sceneario.com/index/coupdecoeur', headers={
        'X-Requested-With': 'XMLHttpRequest'
    })
    soup = BeautifulSoup(f.content, features='lxml')  # lxml is to parse html content

    elements = soup.find_all('img')
    print(elements)

    titles = [e.get('title').replace("Couverture de l'album ", "") for e in elements]

    print(titles)
    pass


if __name__ == '__main__':
    crawl()
