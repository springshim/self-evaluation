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

for doc in docs:
    key = doc.to_dict()
    if key['Full_Name'] == 'Bomi Shim':
        print(key['P_ID'])




app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('name.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('stepcount_fortest.html', name=processed_text)


@app.route('/name/<bomi>')
def hello_name(bomi):
    return render_template('name.html', name=bomi)


@app.route('/step')
def step():
    now = datetime.now()
    data_sum = []

    for x in range(7):
        date = now.strftime("%Y-%m-%d")

        access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkM2WEwiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE2NDE4ODY2ODMsImlhdCI6MTYxMDM1MDY4M30.j3S_fWaAzCyxtuzD-0aR0Z_pc2LqrbjUwHBE1ee_-WQ'
        user_id='6QWR59'

        activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/date/' + date + '.json',
            headers={'Authorization': 'Bearer ' + access_token}).json()
        #pprint(activity_request)

        step = activity_request['summary']['steps']
        goal = activity_request['goals']['steps']
        data_sum.append([date, step, goal])
        data_sum.reverse()
        
        now = now - timedelta(days=1)

    return render_template('step.html', title="Weekly Step Count",
        step=step, goal=goal, step_list=data_sum)



if __name__ == '__main__':
    app.run(debug=True)




'''
@app.route('/')
def hello_world():
    numbers = ['one', 'two', 'three']
    return render_template('list.html', title="Numbers from 1 to 3", my_list=numbers)


@app.route('/rhyme/<word>')
def find_rhymes(word):
    base_url = 'https://api.datamuse.com/words'
    params = { 'rel_rhy':word }
    results = requests.get(base_url, params).json()
    rhy_words = []
    for r in results:
        rhy_words.append(r['word'])
    return render_template('list.html', 
        title="Rhymes with " + word, my_list=rhy_words)

@app.route('<id>')
def login(id):

    return render_template('step.html')



@app.route('/m')
def m():
    html = url_for('static', filename='bigM.png')
    return '<img src='+html+'/>'
'''