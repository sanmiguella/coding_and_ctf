import re

sentiment_analysis = [
    "Boredd. Colddd @blueKnight39 Internet keeps stuffing up. Save me! https://www.tellyourstory.com",
    "I had a horrible nightmare last night @anitaLopez98 @MyredHat31 which affected my sleep, now I'm really tired",
    "im lonely  keep me company @YourBestCompany! @foxRadio https://radio.foxnews.com 22 female, new york"
]

#  \d digit,\w word character, \W special char, \s whitespace
# * zero or more times, + once or more, ? zero or once.
regex_https = r"https\W\W\W\S+.\S+.com"
regex_user_mentions = r"@\S+\d+"

for tweet in sentiment_analysis:
    print(re.findall(regex_https, tweet))
    print(re.findall(regex_user_mentions, tweet))