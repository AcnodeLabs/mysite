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
from datetime import datetime

currentSecond = datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


def todayis():
    return str(currentDay) + '/' + str(currentMonth)+'/'+str(currentYear)


def dtg():
    return str(currentYear) + '_' + str(currentMonth)+'_'+str(currentDay) + 'T' + str(currentHour) + '_' + str(currentMinute)


def gethtml(url):
    headers = {'User-Agent': 'Safari/537.3'}
    req = Request(url=url, headers=headers)
    content = urlopen(req)
    data = content.read()
    return data


allfound = []


def found(j):
    global allfound
    y = json.loads(j.replace("\n", ""))
    allfound.append(y)
    return str(y["offers"]["price"]) + "," + str(y["modelDate"])


def extractCars(soup):
    jsns = soup.find_all('script', {'type': 'application/ld+json'})
    count = 0
    for jsn in jsns:
        s = jsn.string
        if "modelDate" in s:
            found(jsn.string)
            count += 1


def extract(carspec):
    url0 = "https://www.pakwheels.com/used-cars/search/-/"+carspec+"/?page="
    url1 = url0 + "1"
    soup1 = BeautifulSoup(gethtml(url1), features="html.parser")
    try:
        nump = int(soup1.find('li', {'class': 'last next'}).find(
            'a').get('href').split('=')[1])
    except:
        nump = 1
    extractCars(soup1)
    for i in range(2, nump+1):
        urli = url0 + str(i)
        soupi = BeautifulSoup(gethtml(urli), features="html.parser")
        extractCars(soupi)

# returns all gems i.e low price with low mileage


def carstatv(carspec):
    yrl = carspec.split('/yr_')
    yrs = yrl[1]
    y = yrs.split('_')
    frm = y[0]
    fto = y[1]
    av = []
    for year in range(int(frm), int(fto) + 1):
        newspec = yrl[0] + '/yr_'+str(year)+'_'+str(year)
        av.append([newspec, str(carstat(newspec)) + ' Lac Rs'])
    return av


def carstatg(carspec):
    allfound.clear()
    extract(carspec)
    sum = 0
    fsum = 0
    avg = 0
    gems = []
    for car in allfound:
        price = car["offers"]["price"]
        mileageFromOdometer = int(
            car["mileageFromOdometer"].split(' ')[0].replace(',', ''))
        factor = (price / 1000000) * (mileageFromOdometer / 100000)
        sum += car["offers"]["price"]
        fsum += factor

    if sum > 0:
        avg = (int(sum/len(allfound)/10000)/10)
        avgF = fsum/len(allfound)

        for car in allfound:
            price = car["offers"]["price"]
            mileageFromOdometer = int(
                car["mileageFromOdometer"].split(' ')[0].replace(',', ''))
            factor = (price / 1000000) * (mileageFromOdometer / 100000)
            try:
                if (factor < avgF * 0.75):
                    gems.append([car["offers"]["url"], car["image"],
                                 str(car['offers']['price'])])
            except:
                pass
    return gems


def carstat(carspec):
    allfound.clear()
    extract(carspec)
    sum = 0
    fsum = 0
    avg = 0

    for car in allfound:
        price = car["offers"]["price"]
        mileageFromOdometer = int(
            car["mileageFromOdometer"].split(' ')[0].replace(',', ''))
        factor = (price / 1000000) * (mileageFromOdometer / 100000)
        sum += car["offers"]["price"]
        fsum += factor

    if sum > 0:
        avg = (int(sum/len(allfound)/10000)/10)
        avgF = fsum/len(allfound)

        for car in allfound:
            price = car["offers"]["price"]
            mileageFromOdometer = int(
                car["mileageFromOdometer"].split(' ')[0].replace(',', ''))
            factor = (price / 1000000) * (mileageFromOdometer / 100000)
            if (factor < avgF * 0.75):
                gem = car["offers"]["url"]
                if 'islama' in gem:
                    print("Gem::" + gem)
                if 'rawalp' in gem:
                    print("Gem::" + gem)

    print("Avg=" + str(avg) + " Lac for " + carspec)
    return avg


def caravgs(carspec):
    avgs = carstatv(str(carspec).replace('|', '/'))
    return avgs


def oldcargems(carspec):
    gem = carstatg(str(carspec).replace('|', '/'))
    return [carspec, gem]


def oldcarprice(carspec):
    avg = carstat(str(carspec).replace('|', '/'))
    return [carspec, str(avg) + ' Lac Rs']


def getnsav(spec):
    p1 = carstat(spec)
    with open("prius.csv", "a") as f:
        f.write('\n'+dtg()+':'+str(int(p1*100000)))
    return p1


if __name__ == "__main__":
    p1 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2010_2010')
    with open("prius.csv", "a") as f:
        f.write('\n'+dtg()+':'+str(int(p1*100000)))
    p2 = carstat('mk_audi/md_a6/tr_automatic/yr_2019_2019')
    print(p2)
    p2 = carstat('mk_audi/md_a6/tr_automatic/yr_2020_2020')
    print(p2)
    p2 = carstat('mk_audi/md_a6/tr_automatic/yr_2015_2015')
    print(p2)
    p2 = carstat('mk_suzuki/md_ciaz/tr_automatic/yr_2019_2019')
    print(p2)
    p2 = carstat('mk_suzuki/md_ciaz/tr_automatic/yr_2020_2020')
    print(p2)

    # # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2012_2012')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2013_2013')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2014_2014')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2015_2015')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2016_2016')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2017_2017')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2018_2018')
    # p2 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2019_2019')

    print("Upgrade Cost of Prius " + str(p2-p1) + " Lac")
    m1 = carstat('mk_daihatsu/md_move/yr_2011_2011')
    with open("move.csv", "w") as f:
        f.write(str(int(m1*100000)))
    m2 = carstat('mk_daihatsu/md_move/yr_2016_2016')
    # op = carstat('mk_chevrolet/md_optra/tr_automatic/yr_2005_2007')
    # for yr in range(2011,2020):
    #     yrz = 'mk_honda/md_fit/yr_'+str(yr)+'_'+str(yr)
    #     m2 = carstat(yrz)
    print("Upgrade Cost of Move " + str(m2-m1) + " Lac")
    print("Total Upgrade Cost around " + str(int((p2-p1)+(m2-m1))) + " Lac\n")


# SAMPLE
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
