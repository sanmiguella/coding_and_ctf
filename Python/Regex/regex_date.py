import re

sentiment_analysis = [
    "I would like to apologize for the repeated Video Games Live related tweets. 32 minutes ago",
    "@zaydia but i cant figure out how to get there / back / pay for a hotel 1st May 2019",
    "FML: So much for seniority, bc of technological ineptness 23rd June 2018 17:54"
]

#  \d digit,\w word character, \W special char, \s whitespace, \S string
# * zero or more times, + once or more, ? zero or once.
for date in sentiment_analysis:
    regex_time = r"\d{2}\s\S+\s\S+"
    print(re.findall(regex_time, date))

    regex_date = r"\d{1,2}\S{2}\s\S+\s\d{4}\s\d{2}:\d{1,2}"
    print(re.findall(regex_date, date))
