import re

string = "Nice Place to eat! I'll come back! Excellent meat!"

newlist = re.split(r"!", string)

for index, sentence in enumerate(newlist):
    sentence = sentence.strip()

    if sentence != "":
        print(f"({index}). {sentence}")