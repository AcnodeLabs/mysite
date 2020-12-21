import webbrowser
import urllib.parse

from xdatetime import dtg

qr = input("Enter Searchphrase [DuckDuck] :")
qry = urllib.parse.quote(qr)

phrase ="https://duckduckgo.com/?q="
webbrowser.open(phrase+qry, new=2)

strz = dtg() + ',' + qr
with open('searches.csv','a') as fl:
        fl.write(strz + '\n')
        print(strz + ' +>> searches.csv')