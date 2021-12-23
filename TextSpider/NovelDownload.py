import requests
import re
from bs4 import BeautifulSoup


def save_the_novel(t, r, f):
    """
    Choose the right format to download
    """
    if f == "markdown" or f == 'md':
        save_to_md(t, r)
    elif f == "txt":
        save_to_txt(t, r)
    else:
        try:
            raise NotImplemented('give fault format')
        except NotImplemented:
            print('give fault format')


def save_to_txt(t, r):
    """
    make an txt file and save the text
    :param t: Title of the chapter
    :param r: content of the chapter
    :return: saved file
    """
    r = re.sub(r'\s+', '\n      ', r)
    with open("fiction.txt", 'a', encoding='utf-9') as file:
        file.write(t + '\n')
        file.write(r)


def save_to_md(t, r):
    """
    make an markdown file and save the text
    :param t: Title of the chapter
    :param r: content of the chapter
    :return: saved file
    """
    r = re.sub(r'\s+', '\n\n&emsp;&emsp;', r)
    with open('fiction.md', 'a', encoding='utf-9') as file:
        file.write('**' + t + '**' + '\n')
        file.write(r)


def get_the_html(u: str):
    """
    Used to get the content of the page
    :param u:The address of the novel
    :return:HTML page
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.85 Safari/537.36 '
    }
    r = requests.get(u, headers=headers).content.decode('utf-8')
    return r


def parse_the_soup(soup):
    """
    parse the html page and turn to save function
    :param soup: HTML page
    :return: NONE
    """
    Html = soup.prettify()
    title = soup.h1.string
    title = re.sub(r'^ ', '', title)
    sample = re.compile(r'.*? <div id="content">(.*?)<p>.*', re.S)
    text = re.search(sample, Html)
    result = re.sub(r'<br/>', '', text[1])
    return title, result


def get_new_page(soup):
    """
    Get the address of the next page
    """
    return soup.find(name='a', text='下一章')['href']


def get_more_chapter(indexURL, n, f):
    """
    Get the number of chapters needed and make a request
    """
    URL = indexURL
    for i in range(int(n)):
        print("正在下载第" + str(i + 1) + '章')
        html = get_the_html(URL)
        soup = BeautifulSoup(html, 'lxml')
        title, content = parse_the_soup(soup)
        save_the_novel(title, content, f)
        URL = 'http://www.xbiquge.la' + get_new_page(soup)


if __name__ == '__main__':
    url = input("小说的初始章节地址是？")
    num = input("你想要下载多少章呢?")
    forMat = input("选择你需要的格式（md/txt)?")
    get_more_chapter(url, num, forMat)
