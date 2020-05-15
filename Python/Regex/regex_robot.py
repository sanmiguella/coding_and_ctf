import re

sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

# To find only the word robot plus number plus special chars
regex = r'@robot\d\W'

print(re.findall(regex, sentiment_analysis))