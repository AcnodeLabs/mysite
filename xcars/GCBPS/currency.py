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

currentSecond= datetime.now().second
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
#<div class="b1hJbf" data-exchange-rate="166.5">
def getRates():
    url = 'https://www.urdupoint.com/business/open-market-currency-rates-in-pakistan.html'
    soup = BeautifulSoup(gethtml(url),features="html.parser")
    rp = soup.find('p', { 'class' : 'fs14 lh24' }).text.split(' are ')[1].split(',')
    usd = rp[0].split(' PKR ')[1]
    eur = rp[1].split(' PKR ')[1]
    gbp = rp[2].split(' PKR ')[1]
    
    with open('forex.csv',"w") as f:
        print('USD='+usd, end='')
        print(', EUR='+eur, end='')
        print(', GBP='+gbp)
        line = usd+','+eur+','+gbp+'\n'
        f.write(line)
        print(' forex.csv written', flush=True)

if __name__ == "__main__":
    getRates()
    
    
    

# To Improve the code https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# use 'for name,price in zip(names,prices)' to iterate through two list simultaneously