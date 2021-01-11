import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

#################### SELECT DATE #################### 
now = datetime.now()

data_sum = []

for x in range(7):
	date = now.strftime("%Y-%m-%d")
	access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkM2WEwiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE2NDE4ODY2ODMsImlhdCI6MTYxMDM1MDY4M30.j3S_fWaAzCyxtuzD-0aR0Z_pc2LqrbjUwHBE1ee_-WQ'
	user_id='6QWR59'

	activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
		headers={'Authorization': 'Bearer ' + access_token}).json()
#	pprint(activity_request)
	

	step = activity_request['summary']['steps']
	goal = activity_request['goals']['steps']
	data_sum.append([date, step, goal])

	now = now - timedelta(days=1)

for x in data_sum:
	print('date: ', x[0], 'step: ', x[1], 'goal: ', x[2])
