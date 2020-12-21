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
from .xgold import getRate24K10g
from .xdatetime import dtg
import shutil
import itertools

currentSecond = datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

rates = '160.0,,,'
usd = 160.0

# with open('forex.csv', 'r') as fx:
#     rates = fx.readline()
#     usd = float(rates.split(',')[0])


def gethtml(url):
    headers = {'User-Agent': 'Safari/537.3'}
    req = Request(url=url, headers=headers)
    content = urlopen(req)
    data = content.read()
    return data


def pr(sz):
    print(sz, end='', flush=True)


def getPricesEx(brand):
    url = 'http://www.pakwheels.com/new-cars/pricelist/'+brand
    soup = BeautifulSoup(gethtml(url), features="html.parser")
    tables = soup.find_all('table', {
                           'class': 'table table-striped table-bordered orp-event-pricelist nomargin'})
    gold = getRate24K10g()
    names = []
    prices = []
    mlist = []

    for table in tables:
        td1 = table.find_all('td', {'class', 'version-name'})
        td2 = table.find_all('td', {'class', 'version-price generic-green'})
        # <td class="version-name"><a href="/new-cars/suzuki/alto/VX-14/">Suzuki Alto VX</a></td>
        # <td class="version-price generic-green">PKR 1,135,000<a class="show fs12" event-label="Suzuki Alto VX" href="/new-cars/on-road-price?model=alto&amp;version=VX-14">Get On Road Price</a></td>

        for td1x in td1:
            name = td1x.text
            names.append(name)

        for td2x in td2:
            price = td2x.text.split()[1].replace(',', '')
            prices.append(price)

    i = 0
    return list(zip(names, prices))


def getPrices(f, brand):
    pr('.'+brand)
    url = 'http://www.pakwheels.com/new-cars/pricelist/'+brand
    soup = BeautifulSoup(gethtml(url), features="html.parser")
    tables = soup.find_all('table', {
                           'class': 'table table-striped table-bordered orp-event-pricelist nomargin'})
    gold = getRate24K10g()
    names = []
    prices = []

    for table in tables:
        td1 = table.find_all('td', {'class', 'version-name'})
        td2 = table.find_all('td', {'class', 'version-price generic-green'})
        # <td class="version-name"><a href="/new-cars/suzuki/alto/VX-14/">Suzuki Alto VX</a></td>
        # <td class="version-price generic-green">PKR 1,135,000<a class="show fs12" event-label="Suzuki Alto VX" href="/new-cars/on-road-price?model=alto&amp;version=VX-14">Get On Road Price</a></td>

        for td1x in td1:
            name = td1x.text
            names.append(name)

        for td2x in td2:
            price = td2x.text.split()[1].replace(',', '')
            prices.append(price)

    i = 0
    for price in prices:
        f.write(names[i] + "," + price + ',$' + str(int(float(price)/usd)
                                                    ) + ',24k10g ' + str(int(float(price)/gold))+'\n')
        i = i+1


def getAllinFile(fname):
    pr('fetching to '+fname + ' ..')
    f = open(fname, mode='w', encoding='utf-8')
    getPrices(f, 'kia')
    getPrices(f, 'suzuki')
    getPrices(f, 'toyota')
    getPrices(f, 'honda')
    getPrices(f, 'bmw')
    getPrices(f, 'audi')
    getPrices(f, 'hyundai')
    f.close()
    print('..done')


def getAllforDateNow():
    fname = 'carprices-' + dtg() + '.csv'
    getAllinFile(fname)


def getAllforDate(mm, yy):
    fname = 'carprices-' + str(mm) + '-' + str(yy) + '.csv'
    getAllinFile(fname)
    shutil.copy(fname, "carprices.csv")


def getAll():
    getAllinFile("carprices.csv")


if __name__ == "__main__":
    # getAllforDate(currentMonth,currentYear)
    getAllforDateNow()


# To Improve the code https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# use 'for name,price in zip(names,prices)' to iterate through two list simultaneously
