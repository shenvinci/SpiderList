import requests
import re
import os
from universalFunction import getHtml, savePhoto


def downloadPhoto(name, n, p):
    for i in range(int(n/20)+1):
        url = f'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={name}+&pn={n}'
        print("you find the URL:", url)
        r = getHtml(url)
        downloadPic(r, name, (i * 60))


def downloadPic(html, keyword, i):
    pic_url = re.findall('"objURL":"(.*?)",', html.decode('utf-8'), re.S)
    if not os.path.exists(path):
        os.makedirs(path)
    
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            picture = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        p=f"{path}\\{keyword}_{i}.jpg"
        savePhoto(p, picture)
        i += 1


if __name__ == '__main__':
    keyWord = input('gave me the keyword about photo')
    num = int(input("How many photo you want?"))
    path = input("Give the path you want to save photo")
    downloadPhoto(keyWord, num, path)
