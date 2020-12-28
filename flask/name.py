from flask import Flask, render_template, url_for
import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

app = Flask(__name__)

@app.route('/name/<bomi>')
def hello_name(bomi):
    return render_template('name.html', name=bomi)


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


@app.route('/m')
def m():
    html = url_for('static', filename='bigM.png')
    return '<img src='+html+'/>'




@app.route('/step')
def step():
    now = datetime.now()
    data_sum = []

    for x in range(7):
        date = now.strftime("%Y-%m-%d")

        access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJTNkQiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IiwiZXhwIjoxNjA5MjU0MDkzLCJpYXQiOjE2MDkxNjc2OTN9.65eNXO_Zs2XHGKGaI6xAcHWxF7SgtizX65yf8hAVklk'
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

