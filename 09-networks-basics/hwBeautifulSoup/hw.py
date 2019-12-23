import requests
from collections import Counter
from bs4 import BeautifulSoup as bs
import itertools

COOKIE = ""
with open("cookie.txt", "r") as cookie_file:
    for line in cookie_file:
        COOKIE += line.strip()

base_url = "https://pikabu.ru/"
new_subs_url = "https://pikabu.ru/new/subs"
subs_url = "https://pikabu.ru/subs"
commun_url = "https://pikabu.ru/communities/mine"
current_url = f"https://pikabu.ru/new/subs?of=v2&subs=1&_=1577023678973&page=2"
settings_url = "https://pikabu.ru/settings"


HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": 'no-cache',
        "Connection": "keep-alive",
        "Cookie": f"{COOKIE}",
        "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/'
                      '20100101 Firefox/71.0',
    }

change_url = "https://pikabu.ru/new/subs?page=2"

session = requests.Session()

count_articles = 0
page = 0
dict_tegs = {}
my_list = []
# while count < 100:
while count_articles < 100:
    resp = session.get(f"https://pikabu.ru/new/subs?of=v2&subs=1&_=1577034698730&page={page}", headers=HEADERS)
    page += 1
    if resp.status_code == 200:
        soup = bs(resp.content, "html.parser")
        result_my_post = soup.find_all("article", {"class": "story"})
        if not len(result_my_post):
            continue
        result_my_post.pop()
        len_articles = len(result_my_post)
        for i, article in enumerate(result_my_post):
            count_articles += 1
            if count_articles == 5:
                break
            tags = [k.get("data-tag") for k in article.find_all("a", {"class": "tags__tag", "data-tag": True})]
            my_list.append(tags)
            dict_tegs[article.a.text] = tags

itertools_new_my_list = list(itertools.chain.from_iterable(my_list))
counter_words = Counter(itertools_new_my_list)
dict_count_elements = {word: counter_words[word] for word in itertools_new_my_list}
sort_dict_count_elements = sorted(dict_count_elements.items(), key=lambda x: x[1], reverse=True)
print(sort_dict_count_elements)


def final_str_for_writing(sort_dict_count_elements):
    empty_str = ""
    for index, elem in enumerate(sort_dict_count_elements, start=1):
        if index == 11:
            break
        empty_str += f"({index}) {elem[0]} : {elem[1]}\n"
    return empty_str


empty_str = final_str_for_writing(sort_dict_count_elements)

with open("result.txt", "w") as result:
    result.write(empty_str)

