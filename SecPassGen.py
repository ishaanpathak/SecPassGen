"""Secure Password Generator

Contrary to the Program Title, this tool actually generates a secure
Passphrase which instead of using random letters, uses random words.

In order to generate random the tool uses a word list. This generator
uses the Diceware approach to choose the words. Usually this method is
done using a single dice alone or five dice together. The dice(s) are
used to generate truely random sequence of numbers that are then
correlated to the wordlist to get words.

Since true randomness has not been achieved using computers, the tool
actually uses another service to get the random numbers called random.org
"""

import requests
from random import randint
from wordlists import wordlist_en, wordlist_jp


def get_random_numbers(num=4, min=1, max=6, col=5, base=10, format='plain',
    rnd='new') -> list[str]:
    '''Generates a list of sequence of random numbers based on provided
    arguments using https://www.random.org/integers

    Parameters
    ----------
    num : int, optional
        Number of Pairs to Generate
    min : int, optional
        Minimum value of a single generated number
    max : int, optional
        Maximum value of a single generated number
    col : int, optional
        How many values per row of generated values
    base : int, optional
        What base of number to use (2,8,10,16)
    format : str, optional
        Output using Plain Text ('plain') or HTML ('html')
    rnd : str, optional
        What Randomization to use (More information at
        https://www.random.org/faq/#Q2.6)

    Returns
    ----------
    List of strings that are the randomly generated Integer Sequences
    '''
    num *= 5  # We must have 5 Numbers in one sequence for this to work
    url = "https://www.random.org/integers/?num={}&min={}&max={}&col={}"\
          "&base={}&format={}&rnd={}".format(num, min, max, col, base, format,
          rnd)
    content = requests.get(url).content
    output = str(content.decode()).replace('\t', '').split('\n')
    output.pop()
    return output


def generate_password(capitalize=True, include_number=True, separator='=',
    word_count=4, wordlist=wordlist_en) -> str:
    """Generates a secure password using rules provided

    Parameters
    ----------
    capitalize : bool, optional
        Capitalizes the first letter of each word
    include_number : bool, optional
        Includes a random number after one word randomly
    separator : str, optional
        What character to use between each word
    word_count : int, optional
        How many words to use in the password
    wordlist : str, optional
        Which wordlist to use for generating password
    
    Returns
    ----------
    String that is the Generated Password
    """
    keys = get_random_numbers(num=word_count)
    words = list()
    for key in keys:
        words.append(wordlist[key])
    if capitalize:
        for i in range(len(words)):
            words[i] = words[i][0].upper() + words[i][1:]
    if include_number:
        position = randint(1,len(words))-1
        words[position] += str(randint(0, 9))
    password = ""
    for word in words:
        password += word + separator
    return password[:-1]


if __name__=="__main__":
    print(generate_password(word_count=3))