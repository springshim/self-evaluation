import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyAOn5k6mMfyQNJT2K20vCQ2zpxMnh2KtJ8",
  'authDomain': "self-evaluation-f4b63.firebaseapp.com",
  'projectId': "self-evaluation-f4b63",
  'storageBucket': "self-evaluation-f4b63.appspot.com",
  'messagingSenderId': "1002832901774",
  'appId': "1:1002832901774:web:6fffaed9b32547893a3bdf",
  'measurementId': "G-ZYER7VP5BF",
  'databaseURL': "https://self-evaluation-f4b63-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()

'''
filename=input("Enter the name of the file")
cloudfilename=input("File on the cloud")
sotrage.child(cloudfilename).put(filename)
'''

people=db.child("users").child("-MQIstPgllXq569IZffc").get()
print(people.val())




See this video
https://www.youtube.com/watch?v=s-Ga8c3toVY&t=735s