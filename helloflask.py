from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():    
    return '<h1>Hello World!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)