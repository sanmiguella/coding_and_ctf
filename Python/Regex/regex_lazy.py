import re

sentiment_analysis = "Put vacation photos online(They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site(I'm crying)."

#  \d digit,\w word character, \W special char, \s whitespace
# * zero or more times, + once or more, ? zero or once.

brackets_lazy_regex = r"\(.+?\)"
brackets_greedy_regex = r"\(.*?\)"

print(re.findall(brackets_lazy_regex, sentiment_analysis))