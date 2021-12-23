import requests
from bs4 import BeautifulSoup


class ZhiHuEvent:
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content
    
    def __repr__(self):
        return f"标题:{self.title}\n链接:{self.url}"


class ZhiHuSpider:
    def __init__(self):
        self.html = None
        self.data = list()
    
    def __str__(self):
        r = ""
        for event in self.data:
            r += f"{event}\n"
        return r
    
    def get_html(self, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.85 Safari/537.36 ',
            'cookie': cookie}
        answer = requests.get("https://www.zhihu.com/hot", headers=headers).content
        self.html = BeautifulSoup(answer, 'lxml')
    
    def parse_html(self):
        if self.html is None:
            raise
        eventList = self.html.find_all('div', attrs={'class': 'HotItem-content'})
        for event in eventList:
            if event.p:
                self.data.append(ZhiHuEvent(event.h2.string, event.a['href'], event.p.string))


if __name__ == '__main__':
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookies = f.read()
    spider = ZhiHuSpider()
    spider.get_html(cookies)
    spider.parse_html()
    print(spider)
