# Count letters in a string (using collections.Counter
# and it's .most_common method).
import string
import re
from collections import Counter


def main():
    '''Run main function to count letters in a text.'''
    text = 'vrolcntlvunslnenp ineunengeyvlcnemvlcnvxevnvrolcundzuxywtnentzwnywnsrns zvxnewqnuerywtnvxlnmycuvnuvldnv nlvlcweonoymlnyunr znxeflnv nqylnm cneno wtnvyslnvx ztxnvrolcnewqnynglclniluvnmcylwqundl dolneclneogeruneukywtnqyqnynkw gnei zvnvrolcnqzcqlw'

    letters = clear_text(text)

    frequency = Counter(letters)

    print('Частота букв в тексте:')
    print_results(frequency)
    print('Две наиболее встречаемые:')
    print_most_common(frequency)


def clear_text(a_text):
    '''Clear an original text and convert it into a list of letters.'''
    lower_text = a_text.lower().strip(string.punctuation)

    pattern = '[0-9]+'
    no_digits_text = re.sub(pattern, '', lower_text)

    words = no_digits_text.split()
    cleared_words = list()

    for word in words:
        cleared_words.append(word.strip(string.punctuation).replace('\'', ''))

    list_letters = list(''.join(cleared_words))
    print(list_letters)
    return list_letters


def print_results(a_dict):
    '''Print a dictionary of frequency.'''
    for key, value in a_dict.items():
        print(f'{key}: {value:3d} раз(а)')


def print_most_common(a_dict):
    '''Print most common letters.'''
    common_letters = a_dict.most_common(2)

    for key, value in common_letters:
        print(f'{key}: {value:3d} раз(а)')


if __name__ == '__main__':
    main()


text = 'TYLER GETS ME a job as a waiter after that Tylers pushing a gun in my mouth and saying the first step to eternal life is you have to die For a long time though Tyler and I were best friends People are always asking did I know about Tyler Durden'
print(text.lower())

import random
mass = []
while True:
    a = random.randint(1,26)
    b = random.randint(0,26)
    if (4*a + b)%27 == 13:
        mass.append((a,b))
        print(a,b)
    if a == 3 and b == 4:
        mass.append((a, b))
        print(a,b)
        break

print(f'Final a&b keys: {mass}')