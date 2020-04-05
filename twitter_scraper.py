import scrapy, re, logging


class TwitterSpider(scrapy.Spider):
    name = 'twitterspider'
    # start_urls = ['https://mobile.twitter.com/hashtag/covid19']

    def parse(self, response):
        tweets = response.xpath('//table[@class="tweet  "]/@href').getall()
        logging.info(f'{len(tweets)} tweets found')    
        for tweet_id in tweets:        
            tweet_id = re.findall("\d+", tweet_id)[-1]        
            tweet_url = 'https://twitter.com/anyuser/status/'+str(tweet_id)           
            yield scrapy.Request(tweet_url, callback=self.parse_tweet)