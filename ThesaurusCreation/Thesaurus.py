import json

thesaurus = json.load(open("data.json"))


def searchWord(word):
    if word in thesaurus:
        return thesaurus[word]
    else:
        return "The word doesn't exist, please check it again"


inp = input("Enter the word: ")

print(searchWord(inp))
