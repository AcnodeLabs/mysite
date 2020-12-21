from bs4 import BeautifulSoup
import pyautogui as p
import time
from datetime import datetime
import os

def dtg():
    return str(datetime.now().year) + '_'+ str(datetime.now().month)+'_'+str(datetime.now().day) +'T'+ str(datetime.now().hour) + '_'+ str(datetime.now().minute)


b22Mid = [400,400]
hk = 'ctrl'
pth = 'C:\\Users\liveb\Downloads'

def onsaved(fn):
    page = open(pth+'\\'+fn)
    soup = BeautifulSoup(page.read())
    
    if 'You do not meet all the' in soup:
        print('QUAL ERROR')
        

def propose(idtag):
    p.moveTo(b22Mid)
    p.click()
    p.hotkey(hk,'s')
    time.sleep(1)
    fn = 'upfeed_'+idtag+'.html'
    os.system('rm -f '+pth+'\\'+fn)
    p.typewrite(fn+'\n')
    time.sleep(2)
    onsaved(fn)

# propose('01b04c462372e187eb')



# Change https://www.upwork.com/job/Time-Tracking-Android-App-Google-Calendar-Google-Sheet-and-Google-Data-Studio_~0167d3b6369f8237e0/
# TO     https://www.upwork.com/ab/proposals/job/~0181edc838a83957e5/apply/
def lnk(url):
    idtag = url.split('~')[1]
    ret = 'https://www.upwork.com/ab/proposals/job/~'+idtag+'apply/'
    return ret

# print(lnk('https://www.upwork.com/job/Time-Tracking-Android-App-Google-Calendar-Google-Sheet-and-Google-Data-Studio_~0167d3b6369f8237e0/'))
# exit()
brIco = [17,85]
brAddr = [346,76]
mFile = [134,10]


print(dtg())
p.moveTo(brIco)
p.click()
time.sleep(4)
p.moveTo(brAddr)
p.click()
p.typewrite('upwork.com/ab/find-work\n', interval=0.01)
time.sleep(7)
p.hotkey('command','s')
time.sleep(3)
fn = 'upfeed_now'+dtg()
p.typewrite(fn+'.html\n', interval=0.01)
loc = '/Users/imac/Downloads/'+fn
os.system('rm -rf '+loc+'_files')
loc = loc + '.html'

time.sleep(4)
page = open(loc)
soup = BeautifulSoup(page.read())
x = soup.find_all('a', href=True)

for a in x:
    if '/job/' in a['href']:
        os.system('open '+a['href'])






