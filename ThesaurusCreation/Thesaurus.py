import json
from difflib import get_close_matches
thesaurus = json.load(open("data.json"))


def searchWord(word):
    word = word.lower()
    if word in thesaurus:
        return thesaurus[word]
    elif len(get_close_matches(word, thesaurus.keys())) > 0:
        guess = get_close_matches(word, thesaurus.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no " % guess)
        if yn == 'Y':
            return thesaurus[guess]
        elif yn == 'N':
            return "The word %s does not exist in dictionary " % word
        else:
            return "Please enter valid selection from Y/N"
    else:
        return "The word doesn't exist, please check it again"


inp = input("Enter the word: ")

output = searchWord(inp)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
