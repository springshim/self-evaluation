from flask import Flask
app = Flask(__name__)

@app.route('/me')
def index():  
  global ctr
  ctr += 1
  html = str(ctr)
  html += '''
    <p>Name: Bomi Shim</p>
    <p>Hometown: Bucheon</p>
    <p>MSI 2nd student</p>
    <p>Member of intelecto Lab</p>
    <a href='/family'> Go back family page </a>  
    <a href='/friend'> Go back friend page </a>  
    <img src="http://google.com/logos/doodles/2018/fe-del-mundos-109th-birthday-5731929381928960.3-l.png">
	'''
  return html


@app.route('/family')
def about():   
    global ctr
    ctr += 1
    html = str(ctr) 
    html += '''        
    <p>Name: Jia Ko </p>
    <p>Hometown: Changpyung</p>
    <p>Employee</p>
    <a href='/me'> Go back me page </a>  
    <a href='/friend'> Go back friend page </a>    
      '''    
    return html


ctr = 0
@app.route('/friend')
def counter():   
  global ctr
  ctr += 1
  html = str(ctr)
  html += ''' 
  <p>Name: Sohyun Park</p>
  <p>Hometown: Seoul</p>
  <p>Employee</p>
  <a href='/family'> Go back family page </a>  
  <a href='/me'> Go back me page </a>  
'''
  return html

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)
