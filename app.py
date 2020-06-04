import json
from difflib import get_close_matches


def loadWords():
    try:
        data = json.load(open(file='data.json', mode='r'))
        return data
    except FileNotFoundError as ex:
        print("Data File Not Found")


def searchDef(word):
    data = loadWords()
    match = get_close_matches(word, data.keys())
    #   for lower case word
    if word in data:
        return data[word]
    #   for title case word
    elif word.title() in data:
        return data[word.title()]
    #   for upper case word
    elif word.upper() in data:
        return data[word.upper()]
    #   find similar word
    elif len(match) > 0:
        print("\nDid you mean %s instead ? y/n" % match[0], end=' :: ')
        choice = input()
        if choice == 'y' or choice == 'Y':
            print('\nPossible Definitions :: \n')
            num = 1
            for df in data[match[0]]:
                print(str(num)+'.', df)
                num += 1
        else:
            print("\nWord Doesn't Exist In Dictionary")
    else:
        print("\nWord Doesn't Exist In Dictionary")


if __name__ == "__main__":

    print('\n======================================')
    print('<===========> Dictionary <===========>')
    print('======================================')

    word = input('\nEnter A Word :: ')
    num = 1
    define = searchDef(word)
    if define is not None and len(define) > 0:
        print('\nPossible Definitions :: \n')
        for val in define:
            print(str(num)+'.', val)
            num += 1
