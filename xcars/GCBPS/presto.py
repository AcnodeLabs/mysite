from xdatetime import todayis
import xsoup
import xal
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# If you want to open Chrome
driver = webdriver.Chrome('c:\\Users\\liveb\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.prestoexperts.com/post-request/view-requests.aspx')
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
username = driver.find_element_by_id("ctl00_ctl00_BodyPlaceHolder_mainContent_txtEmail")
password = driver.find_element_by_id("ctl00_ctl00_BodyPlaceHolder_mainContent_txtPassword")
username.send_keys("three6tdegree@gmail.com")
mkey = xal.mykey('basepw')
password.send_keys(mkey)
driver.find_element_by_id("ctl00_ctl00_BodyPlaceHolder_mainContent_btnSignIn").click()

print('ok')