import requests
import os

def test():
    url = 'http://m.111.com.cn/maps/index.html?pageId=34&type=release'
    r = requests.get(url)
    with open("demo3.zip", "wb") as code:
        code.write(r.content)

test()
print (os.getcwd())