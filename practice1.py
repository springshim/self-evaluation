import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from datetime import datetime  
from datetime import timedelta

#################### SELECT DATE #################### 


now = datetime.now()

for x in range(7):
    date = now.strftime("%Y-%m-%d")
    print(date)
    now = now - timedelta(days=1)