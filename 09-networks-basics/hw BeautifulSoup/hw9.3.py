import requests
from requests import cookies, Session
from bs4 import BeautifulSoup as bs
from requests.auth import HTTPBasicAuth

base_url = "https://pikabu.ru/"
auth_url = "https://pikabu.ru/@vitomed"
subs_url = "https://pikabu.ru/subs"
raiting_url ="https://pikabu.ru/@vitomed/rating"
NAME = "vitomed"
KEY = "qwerty1234"
data = {"username": NAME, "password": KEY}
headers = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}

cookies = """3:1574450893.5.0.1573126261999:L8tmUw:52.1|862504837.0.2|208439.959546.UWPfbgv_DzZcoP6yRiRWc_18nDg"""


def cookie_jar():
    session = requests.Session()

    jar = requests.cookies.RequestsCookieJar()
    jar.set(
        "sessionid2=3:1574450893.5.0.1573126261999:L8tmUw:52.1|862504837.0.2|208439.959546.UWPfbgv_DzZcoP6yRiRWc_18nDg")
    session.cookies = jar
    r = requests.get(base_url, cookies=cookies)


def auth(base_url, data, headers):
    session = requests.Session()
    session.post(base_url, data=data, headers=headers)
    return session


def Basic_Auth(url, username, key, headers):
    r = requests.post(url, headers, auth=(username, key))
    print(r.text)
    print(r.status_code)


def parse_url(subs_url, headers):
    request = requests.get(subs_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        print(soup)
    else:
        print("Error")


def send_cookie(base_url, headers, cookie):
    cookies = dict(cookies_are=cookie)
    r = requests.post(base_url, headers, cookies=cookies)
    return r


def send_request(username, key):
    session = requests.Session()
    session.auth = (username, key)
    # session.headers.update(headers)
    return session

# auth(base_url, data, headers)
# parse_url(subs_url, HEADERS)
# Basic_Auth(auth_url, NAME, KEY, headers=headers)
# session = send_request(NAME, KEY)
# r = send_cookie(subs_url, headers, cookies)

r = requests.post(subs_url, headers=headers, data=data)
soup = bs(r.text, "html.parser")
print(soup.title)


# print(r.headers)

# r2 = requests.get('https://pikabu.ru/@vitomed', auth=HTTPBasicAuth('vitomed', '81dc9bdb52d04dc20036dbd8313ed055'))

# print(r2.headers)





# if __name__ == "__main__":
# 	picabu = Picabu()
# 	picabu.auth()


"""cookie: yandexuid=4062883181571481168; yuidss=4062883181571481168; _ym_uid=1571918751465071520; 
_ym_d=1571918751; mda=0; fuid01=5db193a111c222c1.yXn4U7lV-mBm3a6f8X-QdXQYrejimfbSxpLBCDZsugFjDnKjGJis-ixTivg2kBOAwOTHAnnGNEz5_VADR5xUXx6PeTb-GT0gRZLRwNAwr14Cvnpmotk9PjTxu2u9Eu7X;
yp=1886841168.yrts.1571481168#1886841168.yrtsi.1571481168#1888486262.udn.cDptZWRpYW5raW4udg%3D%3D; L=c39JSVl3YAZKBm0CDg5FfXRpXV1DZU99JTAGOlcEOBMFWzs=.1573126262.14042.327472.0c58854bed60f7eba028c5ceeb92a9a3;
yandex_login=mediankin.v; i=DB8EvImk1hoMzw2Z5s+MM+Z9UQ5wncqtIizCbXgClLXbodCLy9306QGHuRM/qHSqZP5oiaXDcNnyDN4lBjxE+y2JFYg=; Session_id=3:1574450893.5.0.1573126261999:L8tmUw:52.1|862504837.0.2|208439.737293.KGkPUIrw2J86tbedFejdiRfSR2M; 
sessionid2=3:1574450893.5.0.1573126261999:L8tmUw:52.1|862504837.0.2|208439.959546.UWPfbgv_DzZcoP6yRiRWc_18nDg
"""
