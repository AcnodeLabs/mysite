# import sys
# import subprocess
# import pkg_resources

# required = {'beautifulsoup4', 'urllib3'}
# installed = {pkg.key for pkg in pkg_resources.working_set}
# missing = required - installed

# if missing:
#     python = sys.executable
#     subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen, Request
from datetime import datetime
import shutil
import json

currentSecond = datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


def gethtml(url):
    headers = {'User-Agent': 'Safari/537.3'}
    req = Request(url=url, headers=headers)
    content = urlopen(req)
    data = content.read()
    return data


def xh(name, val):
    return name + "," + val


def xd(name, val):
    v = val.replace(' ', ',').split(',')
    t = v[0]
    ap = v[1][0]
    return name[0][0] + ap + t + "\n"


def praytime(logit=False):
    url = 'https://www.google.com/search?q=prayer+times+islamabad&oq=prayer+times+islamabad&aqs=chrome.0.0l7.8896j0j4&sourceid=chrome&ie=UTF-8'
    soup1 = BeautifulSoup(gethtml(url), features="html.parser")
    # <div class="bsrbZb ptv">4:25 am</div>
    divs = soup1.find_all('td', {'class', 'HlHBvc'})
    divs.pop()  # Remove last empty div
    names = ['Fajr   ', 'Sunrise', 'Zuhr   ',
             'Asr    ', 'Maghrib', 'Isha   ', '', '']
    i = 0
    list = []
    if logit:
        f = open("prayers.csv", "w")
        f2 = open("prayers_"+str(currentDay)+"_"+str(currentMonth)+".csv", "w")
    for d in divs:
        spans = d.find('span').contents[0]
        if logit:
            print(xh(names[i], spans))
            f.write(xd(names[i], spans))
            f2.write(xd(names[i], spans))
        else:
            pair = [names[i].strip(), spans.strip()]
            list.append(pair)
        i += 1
    if logit:
        f.close()
        f2.close()
    return list


if __name__ == "__main__":
    praytime(True)
