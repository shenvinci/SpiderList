import requests
import bs4
from bs4 import BeautifulSoup


def get_new_page(url: str, headers: dict) -> bs4.BeautifulSoup:
    html = requests.get(url, headers=headers).content.decode('utf-8')
    page = BeautifulSoup(html, 'lxml')
    return page


def get_photo_url(page: BeautifulSoup) -> list:
    allFigure = page.find_all('figure')
    linklist = []
    for i in allFigure:
        linklist.append(i.a.get('href'))
    return linklist


def download_photos(page: BeautifulSoup, headers: dict, path: str):
    jpg = page.find('img', id='wallpaper').get('src')
    r = requests.get(jpg, headers=headers)
    with open(path, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.85 Safari/537.36 '
    }
    baseUrl = "https://wallhaven.cc/toplist?page="
    basePath = "E:\\"
    for pageNum in range(1, 3):
        print(f"Now we download the page {pageNum}")
        currentPage = get_new_page(baseUrl + str(pageNum), header)
        photoList = get_photo_url(currentPage)
        num = 1
        for photoUrl in photoList:
            currentPhoto = get_new_page(photoUrl, header)
            download_photos(currentPhoto, header, basePath + f"photo{pageNum}.{num}.jpg")
            num += 1
            print(f"Now download photo in {photoUrl}")
