from .xdatetime import todayis
from .xcurrency import pkr_to_usd
from .xsoup import get_soup


def getRate24K10g():
    sp = get_soup(
        'https://www.urdupoint.com/business/gold-rates-in-pakistan.html')
    r = sp.find('table').find_all('td')[1].text
    rate = r.split(' ')[1].replace(',', '')
    return int(rate)


def getRate24K10gGoogle():
    sp = get_soup(
        'https://www.google.com/search?q=gold+prices+in+pakistan')
    r = sp.find('table').find_all('tr')[3].find_all('div')[2].find('div').text
    rate = r.split(' ')[1].replace(',', '')
    return int(rate)


def getPrice():
    strz = str(getRate24K10g()) + ' on '+todayis()

    with open('gold.csv', 'a') as fl:
        fl.write(strz + '\n')
        print(strz + ' +>> gold.csv')


if __name__ == "__main__":
    print(getRate24K10g())
    getPrice()


# To Improve the code https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# use 'for name,price in zip(names,prices)' to iterate through two list simultaneously
