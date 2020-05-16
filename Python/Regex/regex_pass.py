import re

'''
It can contain lowercase a-z and uppercase letters A-Z
It can contain numbers
It can contain the symbols: *, #, $, %, !, &, .
It must be at least 8 characters long but not more than 20

Great job! Notice that we used the .search() method. The reason is that we want to scan the string to match the pattern. We are not interested in where the regex finds the match.

print("The password {pass_example} is a valid password".format(pass_example=example))
'''

passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

regex = r"[a-zA-Z0-9*#$%!&.]{8,20}"

for example in passwords:
    if re.search(regex, example):
        print(f"The password {example} is a valid password.")
    else:
        print(f"The password {example} is invalid!")
