from secret import fitbit_api_key
import requests
import json

######################### CLASS DEFINITION ###################
class StepCount():
	def __init__ (self, user_id, date, stepcount):
		self.user_id = user_id,
		self.date = date,
		self.stepcount = stepcount



######################### CACHE DATA #########################
CACHE_FNAME = "cache.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def get_unique_key(url):
    return url

def make_request_using_cache(url):
    unique_ident = get_unique_key(url)

    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text 
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

make_request_using_cache
######################### GET FITBIT DATA #########################
def get_fitbit():
	url = 'https://fitbit.com/oauth2/authorize?response_type=code&client_id='
	url_full = url + '22BS6D' + '&scope=activity'

	page_text = make_request_using_cache(url_full)
	print("Hi")

	return url_full

get_fitbit()