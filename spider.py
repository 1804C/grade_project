import requests
import re


class Spider:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def __init__(self, url, **regexs):
        self.url = url
        self.regexs = regexs

    def get_book_info(self):
        r = requests.get(url=self.url, headers=self.headers)
        r.encoding = r.apparent_encoding
        self.book_info = {}
        for key, value in self.regexs.items():
            self.book_info[key] = re.findall(value, r.text)
        return self.book_info


# 链接，需要用到的正则写在这里，直接调用就可以了
url = "https://www.xbiquge6.com/1_1203/#footer"

regex_book = dict(
        regex_author='<meta property="og:novel:author" content="(.*?)"/>',

        regex_book_name='<h1>(.*?)（凡人修仙传仙界篇）</h1>',

        regex_chapter='<dd><a href="/(.*?)">(.*?)</a></dd>',

        )
x = Spider(url=url, **regex_book)
print(x.get_book_info())


