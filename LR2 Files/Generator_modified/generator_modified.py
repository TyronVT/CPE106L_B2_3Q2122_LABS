"""
Program: generator_modified.py
Author: Emmanuel Hayahay & Alaric Espina
Modification of Generator.py by Ken, opens text files to load data necessary for
the creation of the different parts of a sentence
articles -> articles.txt
nouns -> nouns.txt
prepositions -> prepositions.txt
verbs -> verbs.txt
"""

import random

  
def getWords(filename):
    tuple_words = ()
    list_words = []

    # Try opening file clause
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("File Not Found")
        return
    
    # Get all the lines and strip \n
    for line in f:
        stripped_line = line.rstrip()
        list_words.append(stripped_line)
    
    # Close file
    f.close()

    # Convert list to tuple
    tuple_words = tuple(list_words)
  
    # Return tuple
    return tuple_words
 
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""


    number = int(input("Enter the number of sentences: "))
    
    for count in range(number):
        print(sentence())




# The entry point for program execution
if __name__ == "__main__":
    main()

