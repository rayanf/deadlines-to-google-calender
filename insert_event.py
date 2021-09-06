from call_setup import get_calendar_service
import datetime

def create_event(summary,location,description,start_datetime,end_datetime):

    event = {
    'summary': summary, #'Google I/O 2015',
    'location': location , #'800 Howard St., San Francisco, CA 94103',
    'description': description, #'A chance to hear more about Google\'s developer products.',
    'start': {
        'dateTime': start_datetime, #'2015-05-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': end_datetime, #'2015-05-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
    ],
    'attendees': [
        {'email': 'rayanforsast@gmail.com'},
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

def insert_event(event):
    service = get_calendar_service()
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

if __name__ == '__main__':
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    event = create_event('summary test','UT','dexcrip test',now,now)
    insert_event(event)
