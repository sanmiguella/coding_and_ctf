import re

sentiment_analysis = "Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left"

# \d digit, \w word character, \W special char, \s whitespace, \S string
# * zero or more times, + once or more, ? zero or once.
regex_lazy = r"\d+?"
regex_greedy = r"\d+"

print(re.findall(regex_greedy, sentiment_analysis))
