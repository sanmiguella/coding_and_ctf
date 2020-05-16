import re

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

'''
The first part can contain:
Upper A-Z and lowercase letters a-z
Numbers
Characters: !, #, %, &, *, $, .
Must have @
Domain:
Can contain any word characters
But only .com ending is allowed
'''

# \d digit, \w word character, \W special char, \s whitespace, \S string
# * zero or more times, + once or more, ? zero or once.

'''
Great job! Validating strings is a task that becomes simpler when we use regular expressions. Square brackets are very useful for optional characters. Notice that we used the .match() method. The reason is that we want to match the pattern from the beginning of the string.
'''

regex = r"[a-zA-Z0-9!#%&*$.]\S+@\S+.com"

for example in emails:
    if re.match(regex, example):
        print(f"The email {example} is a valid email.")
    else:
        print(f"The email {example} is invalid.")
