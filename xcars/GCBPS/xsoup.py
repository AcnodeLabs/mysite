from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen, Request
import shutil

def get_html(url):
    headers = {'User-Agent': 'Safari/537.3'}
    req = Request(url=url, headers=headers)
    content = urlopen(req)
    data = content.read()
    return data

def get_nth_div(url,n, classtype):
    div = get_soup(url).find_all('div', { 'class' : classtype })[n]
    return div

def get_nth_table(url,n, classtype):
    table = get_soup(url).find_all('table', { 'class' : classtype })[n]
    return table

def get_soup(url):
    soup = BeautifulSoup(get_html(url),features="html.parser")
    return soup