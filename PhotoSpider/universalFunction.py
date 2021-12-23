import requests


def getHtml(url, cookie=None):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.85 Safari/537.36 '
    }
    return requests.get(url, headers=headers).content


def savePhoto(path, pic):
    with open(path, 'wb') as fp:
        fp.write(pic.content)
