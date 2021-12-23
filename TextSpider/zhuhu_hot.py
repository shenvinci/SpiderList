import requests
from bs4 import BeautifulSoup


def get_the_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.85 Safari/537.36 ',
        'cookie': '_zap=6df82fad-8e42-49e6-b3c3-bc3ca2adaa7f; '
                  'd_c0="AICZXLPiGRGPTr0iY27uySDFT7JoLtbSUsE=|1586574925"; '
                  '_ga=GA1.2.311215380.1586574927; _xsrf=wToYS27lG4tBe6ZG10GiI8qhg3H5Y7MP; '
                  'q_c1=57861cc1d82c4ae1ba838f27c1e114c9|1606467054000|1606467054000; '
                  'capsion_ticket="2|1:0|10:1617501289|14:capsion_ticket|44'
                  ':NGMwNjQwZmM5MTUyNDRiNjk2ZmYyZjNmMzJjODU2N2Y'
                  '=|b713148d5ec2ccd665613c48ecc4eb0ceb8bfc3a273f93bd0caea8a87a624a83"; '
                  'captcha_session_v2="2|1:0|10:1617786148|18:captcha_session_v2|88'
                  ':MDI4VFRFREdiUEpsa2VCU1JWZzJaSU9qVUh0REY0N2Z6K3JjOWQ3azhFNmZXWmQ2cE83T1JpcXhDQWpXZ2lCbg'
                  '==|86d79a29990b8a3e9d014a10a7cadcc766443d97b043a2d4a2d8752097843c21"; '
                  '__snaker__id=99hPpSDA9pnWcENs; '
                  'gdxidpyhxdE=8WhWbGDRSGT1Ezoc22SoOcHpgQL%2FYbuXr%5CDSTreB5ivV%2FGxbDOlpPGdUx%2FroJPt7%5CON'
                  '%5CxZ7vEhCKhs1a2yYLGZ0dVQk6zzuMmaRHVQ%2BCQWLofmv6G%5CUlGA9lQ%2F3jOWr%2BkWLMmLbcS7Lc2'
                  '%2B0pc3AfZPE16taEfP%5CcqMpil%5CAX9c4KaRJL%3A1617787048858; _9755xjdesxxd_=32; '
                  'YD00517437729195%3AWM_NI=Abr6Vvrg%2FEEh0RafBPoE30129O9do6i9IpOEx4804QciWv6Yrtgu8NucVwS%2BwVb'
                  '%2FAPsNPNsU6jBoCqpSPVtZiOdM%2FpbovBBpISuY3NgkUf5Z6WfUfxeN4spNEhKVa91oUWg%3D; '
                  'YD00517437729195%3AWM_NIKE'
                  '=9ca17ae2e6ffcda170e2e6ee89db66b891fed4f341bb9a8eb6c14f838e9fafaa618eb3ae89fb6b8b9e86b3c52af0fea7c3b92a83bebed7d57eb2b9e1a6c864f48eaf87c15cad9bfdd1b43afb91f785ee3eabe78791ce4fbcecf8d1b75ba1b79997b553b2aca996bb46b7bd9a98d221b58aaed0c45cb192a0aff25ff6b68e90c27bb48da0b7f752ab91acaeae7ca2b1baa3c17c8b8dbbbab246a5b59b87b852f689aab6e574a792fc94f34687b885b7e433f3b19bb8e637e2a3; YD00517437729195%3AWM_TID=UPhTF3oBirNEVRQRQFdvwI3ex1LYVMAR; z_c0="2|1:0|10:1617786168|4:z_c0|92:Mi4xUVBTbEN3QUFBQUFBZ0psY3MtSVpFU2NBQUFDRUFsVk5Od0tWWUFCUzJYTDh3ZGNlY1ZBV3djU2Q0ZXVrOFRlTXp3|4d282b77674ed59589060d0ec2f4431584239bc227136f60cb4d78718b7ea2ba"; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1619681446,1619851276,1619854807,1619857253; SESSIONID=yr8KNMtdCshLDBydI7ujSq0BhCaJT5FNO4qWV5FIWDR; JOID=U1EXCkJPEBTl05bsPEdQSCXJqOssPmknrpXTk1MEa3eil9ydUysfko3Tlew3hmXUHbuPjPSCZOuuaz-qfuFUrZ4=; osd=WlgSA0xGGRHs3Z_lOU5eQSzMoeUlN2wuoJzalloKYn6nntKUWi4WnITakOU5j2zRFLWGhfGLauKnbjakd-hRpJA=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1619857266; tst=h; KLBRSID=d017ffedd50a8c265f0e648afe355952|1619857315|1619857252 '

    }
    r = requests.get(url, headers=headers).text
    return r


def parse_the_html(h: str) -> tuple:
    soup = BeautifulSoup(h, 'lxml')
    q = soup.find_all(name='h2', attrs={'class': "HotItem-title"})
    a = soup.find_all(name='p', attrs={'class': "HotItem-excerpt"})
    return q, a


def save_to_text(q, a):
    for i, j in zip(q, a):
        print(i)
        with open("hot.txt", 'a', encoding='utf-8') as file:
            file.write('\n'.join([i.string, j.string]))
            file.write('\n' + '==' * 25 + '\n')


if __name__ == '__main__':
    URL = 'https://www.zhihu.com/hot'
    html = get_the_html(URL)
    question, answer = parse_the_html(html)
    save_to_text(question, answer)
