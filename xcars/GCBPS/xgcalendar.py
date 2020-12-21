# THIS FILE HAS BEEN MERGED IN GMAIL.PY, EDIT THERE

from __future__ import print_function
import sys
sys.path.append('.')

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
ted_session = 'Ted Session'

#similiar to?
#Meeting Next: 9:00AM Friday 5-1-2020 GMT+5 On Mon
def is_valid_info(sz):
    key1 = (sz.find('+') > -1) or (sz.find('=') > -1)
    key2 = (sz.find(' ') > -1)
    key3 = (sz.find('-') > -1)
    key4 = (sz.find('5') > -1)
    ok = key1 and key2 and key3 and key4
    return ok

# 9:00AM Friday 5-1-2020 
def get_dtg(snipt, start):
    words = snipt.split(' ')
    m1 = 0
    y = 0
    d = 0
    h = 0
    mn = 0
    for word in words:
        if '-' in word:
            dat = word.split('-')
            m1 = int(dat[0])
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
    hr2 = str(h+3).zfill(2)    
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
    'location': 'XAL office (upper)',
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
        {'method': 'email', 'minutes': 24 * 60},
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
                'C:\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token2.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
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

if __name__ == '__main__':
    # create_event('Meeting Next: 9:00AM Friday 5-1-2020 GMT+5 On Mon')
    create_event('9AM Mon 9-21-2020 GMT+5')
    # main()
