
import requests
from bs4 import BeautifulSoup
import hashlib

host = '178.128.160.242'
port = 32524


with requests.Session() as s:
    # get hash
    html = s.get('http://{}:{}'.format(host, port))
    soup = BeautifulSoup(html.text, 'html.parser')

    # compute md5
    h = soup.h3.string

    html = s.post('http://{}:{}'.format(host, port), data={"hash":hashlib.md5(h.encode('utf-8')).hexdigest()})
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup.p.string)