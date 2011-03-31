from django.shortcuts import render_to_response 
from libs import tehmanis_twitter as twitter

def home(request):
    status = twitter.twitter_status()[:3]
    return render_to_response('main/index.html',{
	'url' : 'home',
	'twitter' : status ,
	})