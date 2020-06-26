import json 
from difflib import get_close_matches
data = json.load(open("076 data.json"))


def translate(word):
    word = word.lower()
    print(word)
    if word in data:
        
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        inputs = input("Did tou mean {0} ?Please input yes or no ".format(get_close_matches(word,data.keys())[0]))
        inputs = inputs.lower()
        if inputs == 'yes':
            return data[get_close_matches(word,data.keys())[0] ]
        elif inputs == 'no': 
            return "The word does not exist, please double check it"
        else:
            return "We did not undertsnd your query"
    else:
        return "The word does not exist, please double check it"

word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item,"\n")
else:
    print(output)