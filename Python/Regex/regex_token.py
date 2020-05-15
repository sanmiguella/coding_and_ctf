import re

sentiment_analysis = "ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever"

#  \d digit,\w word character, \W special char, \s whitespace, \S string
# * zero or more times, + once or more, ? zero or once.

regex = r"#\w+"

no_hashtag = re.sub(regex, "", sentiment_analysis) # replace hashtag with empty space

print(re.split(r"\s+", no_hashtag)) # eliminates whitespaces
