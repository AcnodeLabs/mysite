from __future__ import print_function
import sys
sys.path.append('.')

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import webbrowser
from datetime import datetime
import base64

print('v310520')

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

# If modifying these scopes, delete the file token.pickle.
SCOPESCAL = ['https://www.googleapis.com/auth/calendar']
ted_session = 'Ted Session'

#similiar to?
#Meeting Next: 9:00AM Friday 5-1-2020 GMT+5 On Mon
def is_valid_info(sz):
    key1 = (sz.find('ext') > -1)
    key2 = (sz.find(':') > -1)
    key3 = (sz.find('-') > -1)
    key4 = (sz.find('5') > -1)
    ok = key1 and key2 and key3 and key4
    return ok

def monthcheck(m):
    mm = m.lower()
    if 'jan' in mm:
        return '1'
    if 'feb' in mm:
        return '2'
    if 'mar' in mm:
        return '3'
    if 'apr' in mm:
        return '4'
    if 'may' in mm:
        return '5'
    if 'jun' in mm:
        return '6'
    if 'jul' in mm:
        return '7'
    if 'aug' in mm:
        return '8'
    if 'sep' in mm:
        return '9'
    if 'oct' in mm:
        return '10'
    if 'nov' in mm:
        return '11'
    if 'dec' in mm:
        return '12'
    return m

# 9:00AM Friday 5-1-2020 
def get_dtg(snipt, start):
    words = snipt.split(' ')
    m1 = 0
    y = 0
    d = 0
    h = 0
    mn = 0
    for word in words:
        #Wrote comes after top message
        if 'wrote:' in word:
            break
        if '-' in word:
            dat = word.split('-')
            m1 = int(monthcheck(dat[0]))
            d = int(dat[1])
            y = int(dat[2])
        if ':' in word:
            tt = word[:-2]
            tts = tt.split(':')
            if 'AM' in word:
                h = int(tts[0])
                mn = int(tts[1])
            if 'PM' in word:
                h = int(tts[0]) + 12
                mn = int(tts[1])

    yr = str(y).zfill(4)
    mo = str(m1).zfill(2)
    day = str(d).zfill(2)
    hr = str(h).zfill(2)
    hr2 = str(h+2).zfill(2)    
    mn = str(mn).zfill(2)
    dt = yr + '-'+ mo + '-'+day
    tm = 'T'+ hr + ':' + mn + ":00"
    tme = 'T'+ hr2 + ':' + mn + ":00"
    ofs = '+05:00'
    if (start):
        return dt+tm+ofs
    else:
        return dt+tme+ofs

def get_ev_params_ted(snipt):
    params = {
        'summary' : ted_session,
        'datetime': get_dtg(snipt,True),
        'datetimetill': get_dtg(snipt,False),
    }
    return params

def get_ev_spec(params):
    event = {
    'summary': params['summary'],
    'location': 'Asia',
    'description': 'TED Support',
    'start': {
        'dateTime': params['datetime'],
        'timeZone': 'Asia/Karachi',
    },
    'end': {
        'dateTime': params['datetimetill'],
        'timeZone': 'Asia/Karachi',
    },
    'recurrence': [
        # 'RRULE:FREQ=DAILY;COUNT=2'
    ],
    'attendees': [
        {'email': 'live.bilal.ahsan@live.com'},
        {'email': 'three6tdegree@gmail.com'},
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 6 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    return event

def create_event(snip):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token2.pickle'):
        with open('token2.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\credentials.json', SCOPESCAL)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token2.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Checking upcoming 10 events [173]')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    notFound = True

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if ted_session in event['summary']:
            notFound = False

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
 
    if notFound:
        if (is_valid_info(snip)):
            event = get_ev_spec(get_ev_params_ted(snip))
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        else:
            print(snip+ ' << text did not pass verification to create event xgcalendar.py:118')
    else:
        print(ted_session + ' Event is already in Calendar')


def today():
    return str(currentDay) + "/" + str(currentMonth) + "/" + str(currentYear)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def guruGetProjectUrlFromFullBodyText(txt):
    x = str(txt).split(' (ID:')
    proj_title_1 = x[0].split('none;"> ')[1]
    proj_title_2 = x[1].split('none;"> ')[1]
    j = 'https://www.guru.com/jobs/'
    url1 = j + x[0].split(j)[1].split('"')[0]
    webbrowser.open(url1)
    try:
        url2 = j + x[0+2].split(j)[1].split('"')[0]
        webbrowser.open(url2)
    except:
        print('exception in formula line:218')    
    return proj_title_1 + ' & ' + proj_title_2

def getFullBodyText(service_users__messages, mid):
    res = service_users__messages.get(userId='me',id=mid, format='full').execute()
    msg_str = ''
    if int(res['payload']['body']['size']) > 0:
        msg_str = base64.urlsafe_b64decode(res['payload']['body']['data'].encode('ASCII'))
    elif int(res['payload']['parts'][0]['body']['size']) > 0:
        msg_str = base64.urlsafe_b64decode(res['payload']['parts'][0]['body']['data'].encode('ASCII')).decode("utf-8")
    return msg_str              

def findFirstFrom(msgs, mfrom):
    id0 = msgs.list(userId='me',q='from:'+mfrom).execute().get('messages',[])[0]['id']
    return msgs.get(userId='me',id=id0).execute()['snippet']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    print('fetching ..',end='')
    msgs = service.users().messages()
    results = msgs.list(userId='me',q='is:unread').execute()
    #Get FirstOf
    print('\nLast Messages from Important Clients:')
    tedsnip = findFirstFrom(msgs,'jiang.ted@gmail.com')
    print('Ted Said: '+ tedsnip)
    create_event(tedsnip)
    print('Fred Said: '+findFirstFrom(msgs,'fred@perfectcircle.com'))
    ##
    labels = results.get('messages', [])

    if not labels:
        print('No Messages found.')
    else:
        print('parsing ..')
        cnt = 0
        tot = 0
        bnk = []
        guru = []
        meetings = []
        for label in labels[:20]:
            lid = label['id']
            res = msgs.get(userId='me',id=lid).execute()
            hdrs = res['payload']['headers']
            id = res['id']
            froms = []
            subjs = []
           

            for hdr in hdrs:
                nam = hdr['name']
                val = hdr['value']
                if nam=='From':
                    froms.append(val)
                if nam=='Subject':
                    subjs.append(val)
            
            for f,s in zip(froms,subjs):
                if '@guru' in f:
                    print('!', end='')
                    guru.append(id)
                if 'Bank' in s:
                    print('$', end='')
                    bnk.append(id)
                if '@payoneer' in f:
                    print('\n')
                    print(f,end='\t')
                    print(s)
                    cnt += 1
                if 'ted@' in f:
                    print('m')
                    meetings.append(id)
                    cnt += 1
                if '@upwork' in f:
                    print('\n')
                    print(f,end='\t')
                    print(s)
                    cnt += 1
                if 'ayment' in f:
                    print('\n')
                    print(f,end='\t')
                    print(s)
                    cnt += 1
                if 'fred@' in f:
                    print('\n')
                    print(f,end='\t')
                    print(s)
                    cnt += 1
                if '@' in f:
                    tot += 1
        print("\n"+str(cnt)+" Important out of unread "+ str(tot), flush=True)
       
        for g in guru:
            txt = guruGetProjectUrlFromFullBodyText(getFullBodyText(msgs, g))
            print('guru jobs check::['+txt+']')

        for m in meetings:
            snp = msgs.get(userId='me',id=m).execute()['snippet'].split(',')
            txt = snp[0]
            if ('-' not in txt):
                txt = txt + ' '+ snp[1]
            create_event(txt)
            print('Meeting ' + txt)

        with open("bank.csv","a") as f:
            for b in bnk:
                res = msgs.get(userId='me',id=b).execute()
                txt = getFullBodyText(msgs, b)           
                if 'withdrawn' in txt:
                    bal = txt.split('PKR')[2].replace('\r\n','').split(' ')[0].replace(',','')
                    acct = res['snippet'].split('A/C: ')[1].split(',')[0]
                    print(bal + ' PKR in '+acct) 
                    f.write(today()+','+acct+','+bal+"\n")
                elif 'Fund Transfer' in txt:                
                    print(txt, end='')
                elif 'bill payment' in txt:                
                    print(txt, end='')
                elif 'Financial Pin' in txt:                
                    print('', end='')
                elif 'IBFT' in txt:
                    print('InterBank Transfer:'+txt)
                elif 'POS' in txt:                
                    print('POS Transaction:'+txt)
                elif 'login access code' in txt:                
                    print('login access code:'+txt.split('code is ')[1].split(' ')[0])
                else:
                    print('Could not Identify Decode TXT='+txt)
        if cnt>0:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

if __name__ == '__main__':
    main()