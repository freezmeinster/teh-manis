from django.shortcuts import render_to_response 
from django.template import RequestContext

def home(request):
   # status = twitter.twitter_status()[:3]
    return render_to_response('main/index.html',{
	'url' : 'home',
	#'twitter' : status ,
	},context_instance=RequestContext(request))