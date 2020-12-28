import fitbit
from secret import client_id, client_secret

# You'll have to gather the tokens on your own, or use
# ./gather_keys_oauth2.py
authd_client = fitbit.Fitbit(client_id, client_secret,
                             access_token='<access_token>', refresh_token='<refresh_token>')
authd_client.activities()



unauth_client = fitbit.Fitbit(client_id, client_secret)
# certain methods do not require user keys
unauth_client.activity_units()