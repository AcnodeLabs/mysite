# import sys
# import subprocess
# import pkg_resources

# required = {'beautifulsoup4', 'urllib3'}
# installed = {pkg.key for pkg in pkg_resources.working_set}
# missing = required - installed

# if missing:
#     python = sys.executable
#     subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from carstats import *

def caravgprice()

if __name__ == "__main__":
    ciaz = carstat('mk_suzuki/md_ciaz/tr_automatic/yr_2017_more')
    alpha = carstat('mk_toyota/md_prius-alpha/yr_2015_more')
    p1 = carstat('mk_toyota/md_prius/vr_s-1-8/yr_2010_2010')
    p2 = carstat('mk_toyota/md_prius/yr_2015_2015')
    print("Upgrade Cost of Prius " +str(p2-p1)+ " Lac")
    m1 = carstat('mk_daihatsu/md_move/yr_2011_2011')
    m2 = carstat('mk_daihatsu/md_move/yr_2016_2016')
    print("Upgrade Cost of Move " +str(m2-m1)+ " Lac")
    print("Total Upgrade Cost around " +str(int((p2-p1)+(m2-m1)))+ " Lac\n")
    
    
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