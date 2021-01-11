import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

#################### SELECT DATE #################### 



date='2020-12-20'

'''
activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
    headers={'Authorization': 'Bearer ' + access_token}).json()
pprint(activity_request)
'''

activity_request = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1min.json',
    headers={'Authorization': 'Bearer ' + access_token}).json()
pprint(activity_request)


try:
	response = \
	requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1min.json',
		headers={'Authorization': 'Bearer '
                     + FITBIT_ACCESS_TOKEN,
                     'Accept-Language': FITBIT_LANGUAGE})
    response.raise_for_status()
except requests.exceptions.HTTPError, err:
    print 'HTTP request failed: %s' % err
    sys.exit()

data = response.json()
print 'Got heartrates from Fitbit'