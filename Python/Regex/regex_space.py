import re

string = "He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready"

# \d digit,\w word character, \W special char, \s whitespace
regex = r"\W\dbreak\W"

string = re.sub(regex, " ", string)
print(string)

regex = r"\Wnew\w"

string = re.sub(regex, " ", string)
print(string)