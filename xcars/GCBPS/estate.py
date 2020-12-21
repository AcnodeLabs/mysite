from xdatetime import todayis
from xcurrency import pkr_to_usd
from xgold import getRate24K10g
import xsoup

def getPrices9D():
    table = xsoup.get_nth_table('https://dha-city.com/plot-prices/',0,'tablepress tablepress-id-4')
    tr9D = table.find_all('tr')[32]
    sectorname = tr9D.find_all('td')[0].text
    sectorprice = tr9D.find_all('td')[4].text
    lac = int(sectorprice.split(' ')[0])
    gold = getRate24K10g()
    strz = '9D is '+ sectorprice + ' i.e ' + str(pkr_to_usd(lac * 100000)) + '$ i.e '+str(int((lac*1000000)/gold))+' 24K10g on '+ todayis()

    with open('9D.csv','a') as fl:
        fl.write(strz + '\n')
        print(strz + ' +>> 9D.csv')

if __name__ == "__main__":
    getPrices9D()
  
   

# To Improve the code https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# use 'for name,price in zip(names,prices)' to iterate through two list simultaneously