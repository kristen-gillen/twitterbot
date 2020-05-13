import tweepy
#information kept local for security
auth = tweepy.OAuthHandler('private', 'private')
auth.set_access_token('private', 'private')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
#Calls the decorator function then uses the tweepy cursor on followers, and then items to make an iterable
for follower in limit_handle(tweepy.Cursor(api.followers).items()): #call the decorator function to help overloading the calls to API
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()
    #break - can add here if long list

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
   
    try:
        tweet.favorite()
        #or could retweet here
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break