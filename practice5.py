import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

### add data ###
#db.collection('persons').add({'name':'John', 'age' : 50})


### read data ###
### 하나만 가져올 때 ###
#if result.exists:
#	print(result.to_dict())
#	name = result.to_dict()
#	print(name['Jane'])


### 여러개 가져올 때 ###

docs = db.collection('users').get()

for doc in docs:
	key = doc.to_dict()
	#print(key)
	if key['Full_name'] == 'Bomi Shim':
		#print(key['Full_name'])
		access_token = key['Access_token']
		user_id = key['User_ID']


print(access_token)
print(user_id)