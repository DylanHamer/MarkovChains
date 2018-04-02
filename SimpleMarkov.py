"""
SimpleMarkov.py
Simple markov chain example
By Dylan Hamer
"""

import markov  # My markov generator module
import sys

inputFile = sys.argv[1]

def main():
    corpus = markov.getCorpus(inputFile)
    chain = markov.generateMarkov(corpus, 50)
    print(" ".join(chain))

main()
