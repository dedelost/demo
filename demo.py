import requests
import os

def testver():
    url = 'http://192.168.1.101:5000/101'
    r = requests.get(url)
    print(r.content)
    if 1:
        test()

def test():
    url = 'http://127.0.0.1:5000/100'
    r = requests.get(url)
    with open("%sdemo3.txt" % 'test', "wb") as code:
        code.write(r.content)
        tests()

def tests():
    if not os.path.exists(r'testdemo3.txt'):
        print('update success!')

testver()
# test()
print (os.getcwd())