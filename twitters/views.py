#from django.shortcuts import render
#from django.http import HttpResponse
#from __future__ import unicode_literals
from django.http import JsonResponse 
from urllib.parse import quote
from allauth.socialaccount.admin import SocialApp
import oauth2
import json
# Create your views here.
CONSUMER_KEY ="JOp5t7DapP5HijinscAVul7kB"
CONSUMER_SECRET ="MK7UWGuDt8qnub94SE9jlJ1v1wCC0T7Ucqz7cHzECVbfVXRFth"

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, http_method, bytes(post_body, "utf-8"), headers=http_headers )
    return content


def tweetsearch(request):
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id) 
	app_token = social_account.socialtoken_set.get(account=social_account.id)
	token = app_token.token
	token_secret =app_token.token_secret
	
	query="busalo7"
	enc_q=quote(query)
	url="https://api.twitter.com/1.1/search/tweets.json?q=%s"%(enc_q)
	

	response = oauth_req(url,token,token_secret, "GET")
	print(response)

	stuff= json.loads(response.decode('utf-8')) # got problem Json added .decode('utf-8')after response
	return JsonResponse(stuff,safe=False)
