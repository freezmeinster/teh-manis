from libs import oauth2
from libs.twitter import twitter

consumer_key = 'dTHMFjpQDhg0ab83e7w'
consumer_secret='OZel8tb0tyJYUa0s642IdyiJcZJq29C5pAuSTaqO7Y'
access_token_key='275902931-05SoYwxmFhiBxaSVuAqNj9TANLG0sFtMMHhOGawF'
access_token_secret='u7VVjbQ4XcK2MTe1p6JYTc0kimozvEaAJhIr3iok'
twitter_user = 'freez_meinster'
max_last_status = 3

def twitter_status( request ):
    api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
    )
    
    status = api.GetUserTimeline(twitter_user)[:max_last_status]
    return { 'tweet' : status }
