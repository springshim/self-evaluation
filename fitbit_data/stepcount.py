import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from flask import Flask, render_template, url_for


access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJTNkQiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE2MDE2NzI1NzIsImlhdCI6MTYwMTA2Nzc3Mn0.azG8ieS_EqHK6seqZDq_RNlrAovnvOpqs66nWdiGFn4'
user_id='6QWR59'


activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/2020-09-23.json',
	headers={'Authorization': 'Bearer ' + access_token})
"""



print(activity_request.status_code)
#print(activity_request.text)
pprint(activity_request.json()['activities'])
"""


app = Flask(__name__)

@app.route('/')
def step_count():
	results = activity_request.json()
	results = results['activities'][0]

	print("###############################")
	print(results)
	print("###############################")

	res = []
	res = [{'startDate':i['startDate'],'steps':i['steps']} for i in startDate][:7]

	return render_template('main.html', startDate = startDate, steps = steps)


if __name__ == '__main__':
	app.run(debug=True)