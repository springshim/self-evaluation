from flask import Flask, render_template, url_for
from flask import request
import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
docs = db.collection('users').get()

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('name.html')

@app.route('/', methods=['POST'])
def my_form_post():
    now = datetime.now()
    data_sum = []

    processed_text = request.form['text']

    for doc in docs:
        key = doc.to_dict()
    if(processed_text):
        if key['Full_name'] == processed_text: 
            access_token = key['Access_token']
            user_id = key['User_ID']

            for x in range(7):
                date = now.strftime("%Y-%m-%d")
                specified_date = now.strftime("%Y-%m-%d [%a]")

                activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
                    headers={'Authorization': 'Bearer ' + access_token}).json()

                step = activity_request['summary']['steps']
                goal = activity_request['goals']['steps']
                data_sum.append([specified_date, step, goal])
                data_sum.reverse()
                
                now = now - timedelta(days=1)

            return render_template('step.html', title="Weekly Step Count",
                step=step, goal=goal, step_list=data_sum, user_id=user_id, access_token=access_token)
        else:
            message = 'Unregistered Name. Check whether you put the wrong upper case in your name.'
            return render_template('name.html', message=message)        


if __name__ == '__main__':
    app.run(debug=True)


