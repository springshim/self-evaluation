import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

#################### SELECT DATE #################### 
now = datetime.now()

for x in range(7):
	date = now.strftime("%Y-%m-%d")
	print(date)

	access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJTNkQiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IiwiZXhwIjoxNjA4OTI4MzU4LCJpYXQiOjE2MDg4NDIxNTF9.2NbX-At4-Hj7z0Yx1eMk7CgHUCJVc38llpDtwpedo10'
	user_id='6QWR59'

	activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
		headers={'Authorization': 'Bearer ' + access_token}).json()
	#pprint(activity_request)

	step = activity_request['summary']['steps']
	goal = activity_request['goals']['steps']
	print("Step: ", step, "Goal: ", goal)
	now = now - timedelta(days=1)
