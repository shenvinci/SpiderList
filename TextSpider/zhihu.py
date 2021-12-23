import requests
from bs4 import BeautifulSoup


def get_the_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.85 Safari/537.36 '
    }
    r = requests.get(url, headers=headers).text
    return r


def parse_the_html(h: str) -> tuple:
    soup = BeautifulSoup(h, 'lxml')
    q = soup.find_all(name='a', attrs={'class': "ExploreCollectionCard-contentTitle"})
    a = soup.find_all(name='div', attrs={'class': "ExploreCollectionCard-contentExcerpt"})
    return q, a


def save_to_text(q, a):
    for i, j in zip(q, a):
        with open("zh.txt", 'a', encoding='utf-8') as file:
            file.write('\n'.join([i.string, j.string]))
            file.write('\n' + '==' * 25 + '\n')


if __name__ == '__main__':
    URL = 'https://www.zhihu.com/explore'
    html = get_the_html(URL)
    question, answer = parse_the_html(html)
    save_to_text(question, answer)
