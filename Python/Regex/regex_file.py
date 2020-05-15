import re

sentiment_analysis = [
    "AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company",

    "ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year" 
]

#  \d digit,\w word character, \W special char, \s whitespace, \S string
# * zero or more times, + once or more, ? zero or once.
# [a-zA-Z] -> a to z or A to Z {2} -> 2 chars
# \S+.txt -> *string*.txt
regex = r"^[a-zA-Z]{2}\S+.txt"

for text in sentiment_analysis:
    print(re.findall(regex, text))
    print(re.sub(regex, "", text))
