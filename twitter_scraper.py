from twitter_scraper import get_tweets

for tweet in get_tweets('covid19', pages=1):
    print(tweet['text'])