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
p_id_list = []

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
            p_id = key['P_ID']

            for x in range(7):
                date = now.strftime("%Y-%m-%d")
                specified_date = now.strftime("%Y-%m-%d [%a]")

                activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
                    headers={'Authorization': 'Bearer ' + access_token}).json()

                step = activity_request['summary']['steps']
                goal = activity_request['goals']['steps']
                data_sum.append([specified_date, step, goal])
                
                now = now - timedelta(days=1)

            
            p_id_list.clear()
            p_id_list.append(p_id)
            return render_template('step.html', title="Weekly Step Count",
                step=step, goal=goal, step_list=data_sum, user_id=user_id, p_id=p_id, access_token=access_token)
        else:
            message = 'Unregistered Name. Check whether you put the wrong upper case in your name.'
            return render_template('name.html', message=message)        


@app.route('/autonomy1')
def autonomy1():
    p_id = p_id_list
    return render_template('autonomy1.html', p_id=p_id)

@app.route('/autonomy2')
def autonomy2():
    p_id = p_id_list
    return render_template('autonomy2.html', p_id=p_id)

@app.route('/success')
def success():
    p_id = p_id_list
    return render_template('success.html', p_id=p_id)



@app.route('/efficacy1')
def efficacy1():
    p_id = p_id_list
    return render_template('efficacy1.html', p_id=p_id)



if __name__ == '__main__':
    app.run(debug=True)


