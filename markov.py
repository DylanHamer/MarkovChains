"""
SimpleMarkov.py
Simple markov chain module
By Dylan Hamer
"""

from random import choice  # Choose random words

def getCorpus(filename):
    """Open a file and split it into an array"""
    with open(filename) as fileObject:
        fileContents = fileObject.read()  # Read contents of array
    corpus = fileContents.split(" ")  # Split file contents into array
    return corpus


def generatePairs(corpus):
    """Split corpus into two word tuples and return them as a generator"""
    for index in range(len(corpus)-1):  # Iterate through all but the last item in the corpus
        pair = (corpus[index], corpus[index+1])  # Make a pair
        yield pair


def generateWordlist(pairs, corpus):
    """Generate a dictionary that stores the pairs of words and their probabilities"""
    wordlist = {}  # Dictionary to store words
    for firstWord, secondWord in pairs:
        if firstWord in wordlist:  # If the word is already in the list of words
            wordlist[firstWord].append(secondWord)  # Add second word to the array of words succeeding it
        else:  # If the word is not in the list of words
            wordlist[firstWord] = [secondWord]  # Add it to the dictionary as an array
    return wordlist


def generateChain(wordlist, corpus, size):
    """Generate the Markov chain"""
    firstWord = choice(corpus)
    chain = [firstWord]  # Start the chain with a random word

    for count in range(size):  # Make a chain with a specified size
        word = choice(wordlist[chain[-1]])  # Choose a random word from the wordlist
        chain.append(word)  # Add the word to the chain
    return chain


def generateMarkov(corpus, size):
    pairs = generatePairs(corpus)
    wordlist = generateWordlist(pairs, corpus)
    chain = generateChain(wordlist, corpus, size)
    return chain
