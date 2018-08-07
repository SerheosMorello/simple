import requests
from lxml import html
from io import StringIO

def test():
    return "Hi"
sayhi = test()

def getStatus_code(url):
    return requests.get(url).status_code

def getElement(url, tag, value):
    r = requests.get(url)
    root = html.parse(StringIO(r.text)).getroot()
    links = root.cssselect(tag)
    for link in links:
        if link.text == value:
            return True
    return False
