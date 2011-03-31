from libs import oauth2
from libs.twitter import twitter

consumer_key = 'Y3UimF6A2FRzB3gFmYg7Q'
consumer_secret='4CJqP9JcFVcMZxnk3coscT5TUht0iHUrVH4I1Qpjk'
access_token_key='79429095-feDqXDJg0u2wDGRfI0Zm0JmOID4WJlvylk4SBFkLC'
access_token_secret='wBvXbSHrhaDzxRFwVMP4EMUU6AO5LRsxg4b3aIhIY'
twitter_user = 'freez_meinster'

def twitter_status():
    api = twitter.Api(
	consumer_key=consumer_key,
	consumer_secret=consumer_secret,
	access_token_key=access_token_key,
	access_token_secret=access_token_secret
	)
	
    status = api.GetUserTimeline(twitter_user)
    return status
