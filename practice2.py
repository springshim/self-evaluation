'''
my_string="hello python world , i'm a beginner "
print (my_string.split("world",1)[1] )
'''

#Access Token만 추출해내는 방법

'''
full_url = 'http://127.0.0.1:8080/#access_token=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkM2WEwiLCJzdWIiOiI2UVdSNTkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE2NDE4ODY2ODMsImlhdCI6MTYxMDM1MDY4M30.j3S_fWaAzCyxtuzD-0aR0Z_pc2LqrbjUwHBE1ee_-WQ&user_id=6QWR59&scope=activity+profile&token_type=Bearer&expires_in=31536000'
full_url = full_url.split("access_token=",1)[1]
full_url = full_url.split("&")[0]

print(full_url)
'''

#함수 밖에서도 값을 저장할 수 있나?
#append 사용시 가능

db = [3, 5, 7]
print(db)

def test():
	db2 = 4
	db.append(db2)

test()

dp = db[-1]

print(dp)