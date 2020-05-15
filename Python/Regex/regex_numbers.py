import re

string = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

# \d digit,\w word character,\s whitespace
regex = r'User_mentions:\d'
user_mentions = re.findall(regex, string)

regex = r'likes:\s\d'
likes = re.findall(regex, string)

regex = r"number\sof\sretweets:\s\d"
retweets = re.findall(regex, string)

for user_mention, like, retweet in zip(user_mentions, likes, retweets): 
    user_mention = user_mention.strip()
    like = like.strip()
    retweet = retweet.strip()

    print(user_mention)
    print(like)
    print(retweet)
