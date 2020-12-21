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

allfound = []

def found(j):
    global allfound
    y = json.loads(j.replace("\n",""))
    allfound.append(y)
    return str(y["offers"]["price"]) + "," + str(y["modelDate"])

def extractCars(soup):
    jsns = soup.find_all('script', {'type':'application/ld+json'})
    count = 0
    for jsn in jsns:
        s = jsn.string
        if "modelDate" in s:
            found(jsn.string)
            count += 1

def extract(carspec):
    url0 = "https://www.pakwheels.com/used-cars/search/-/"+carspec+"/?page="
    url1 = url0 + "1"
    soup1 = BeautifulSoup(gethtml(url1),features="html.parser")
    try:
        nump = int(soup1.find('li', { 'class' : 'last next' }).find('a').get('href').split('=')[1])
    except:
        nump = 1
    extractCars(soup1)
    for i in range(2,nump+1):
        urli = url0 + str(i)
        soupi = BeautifulSoup(gethtml(urli),features="html.parser")
        extractCars(soupi)

def carstat(carspec):
    allfound.clear()
    extract(carspec)
    sum = 0
    mil = 0
    for car in allfound:
        sum += car["offers"]["price"]
        km = car["mileageFromOdometer"]
        r= km.replace(' ',' ').replace(',',' ').replace('km',' ').replace(' ','')
        mil += int(r)
    if (sum<=0):
        return 0
    avg = (int(sum/len(allfound)/10000)/10)
    avgk = int(mil/len(allfound))
    print("Avg Price=" + str(avg)+ " Avg Km=" + str(avgk) + " for " + carspec )
    return avg

def get(car,yr):
    return carstat(car+'/yr_'+str(yr)+'_'+str(yr))

if __name__ == "__main__":
    carspec = 'mk_toyota/md_prius'
    for y in range(2019-9,2019):
        p1 = get(carspec,y)
        
    
#SAMPLE
# {
# 	"@context": "https://schema.org",
# 	"@type": "Car",
# 	"brand": {
# 		"@type": "Brand",
# 		"name": "Toyota"
# 	},
# 	"description": "Toyota Prius 2015 for sale in Islamabad",
# 	"itemCondition": "used",
# 	"modelDate": 2015,
# 	"manufacturer": "Toyota",
# 	"fuelType": "Petrol",
# 	"name": "Toyota Prius 2015 for sale in Islamabad",
# 	"image": "https://cache4.pakwheels.com/ad_pictures/3533/toyota-prius-s-1-8-2015-35330158.jpg",
# 	"vehicleTransmission": "Automatic",
# 	"vehicleEngine": {
# 		"@type": "EngineSpecification",
# 		"engineDisplacement": "1800cc"
# 	},
# 	"mileageFromOdometer": "75,392 km",
# 	"offers": {
# 		"@context": "https://schema.org",
# 		"@type": "Offer",
# 		"price": 3550000,
# 		"availability": "http://schema.org/InStock",
# 		"priceCurrency": "PKR",
# 		"url": "https://www.pakwheels.com/used-cars/toyota-prius-2015-for-sale-in-islamabad-3657682"
# 	}
# }   