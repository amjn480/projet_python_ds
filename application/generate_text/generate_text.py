import math
import numpy as np
import random
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(os.path.dirname(path_script)))

eps = 1e-6


def generate_bigramme(language, lenght_sentence):

    """Generate a sequence of coherent letters using the transition matrix of bigrams for a language.
    Parameters :
    length_sentence : the length of the sequence"""

    # Data importation
    matrix = np.loadtxt(path_root + f"/training/Matrix/Matrix_{language}.txt")
    freq = np.loadtxt(path_root + f"/training/Frequency/Frequencies_{language}.txt")
    # First letter
    current_state = random.choices(range(len(matrix)), weights=freq)[0]
    generated_text = chr(current_state)
    
    for _ in range(1, lenght_sentence):
        # We take a randomly weighted letter based on transition probabilities which will be the next letter
        next_state = random.choices(range(len(matrix)), weights=matrix[current_state])[0]
        generated_text += chr(next_state)
        current_state = next_state

    return generated_text


def generate_trigramme(language, lenght_sentence):
    """Generate a sequence of coherent letters using the transition matrix of trigrams for a language.
    Parameters :
    length_sentence : the length of the sequence"""
    # Load the transition matrix and frequencies
    matrix2 = np.loadtxt(path_root + f"/training/Matrix/Matrix_Trigramme_{language}.txt")
    freq = np.loadtxt(path_root + f"/training/Frequency/Frequencies_{language}.txt")
    rows_to_keep = np.array([32] + list(range(97, 123))+list(range(224, 255))) #We keep the letters we have chosen to keep
    freq = freq[np.ix_(rows_to_keep)]
    #Selection of the first letter
    current_state2 = random.choices(range(len(freq)), weights=freq)[0]

    while current_state2 == -1: # If it is true, then it is a character that we don't want so we have to change it
        current_state2 = random.choices(range(60), weights=freq)[0]   
    current_state = current_state2*60 
    generated_text = decode(current_state)

    for _ in range(1, lenght_sentence):  
        #Selection of the next letter
        nb = random.choices(range(len(matrix2)), weights=matrix2[current_state])[0]  
        nb1 = nb % 60 # Corresponds to the ord of the first character
        nb2 = nb//60 # Corresponds to the ord of the second character
        while revient(nb2) == -1:
            nb = random.choices(range(len(matrix2)), weights=matrix2[current_state])[0]
            nb2 = nb//60
            nb1 = nb % 60
        next_state = nb  
        # We decode the number to convert it in a str
        generated_text += decode(next_state)[1]
        current_state2 = nb2
        current_state = nb
    return generated_text


def perplexity(text, language):

    """Measure the plausibility of a text."""

    matrix = np.loadtxt(path_root + f"/training/Matrix/Matrix_{language}.txt")
    res = 0
    c1 = text[0]
    for c2 in text[1:]:
        i = ord(c1)
        j = ord(c2)
        res += math.log(matrix[i, j] + eps)
        c1 = c2
    return res


def revient(nb):
    """Brings characters back into the correct intervals for ASCII tables.
    """
    # Space is encoded as 0 in our matrix and 32 in ASCII characters.
    if nb == 0:
        return 32
    # Numbers between 97 and 122 are lowercases letters in ASCII tables.
    elif nb <= 26:
        return nb+96
    # Numbers between 224 and 255 are lowercases letters with accent
    elif nb <= 58:
        return nb+197
    # For all others letters we have decided not to count them since they doesn't appear often
    else:
        return -1


def decode(nb):
    """Converts a number into its associated character string."""
    # If nb==-1, then we don't keep this character
    if nb < 0:
        return -1
    # Else we convert the  number into a string chain
    c = ''
    c += chr(revient(nb % 60))
    c += chr(revient(nb//60))
    return c


# To generate sentences with the bigramme model and the trigramme model

print(generate_bigramme(language='fr', lenght_sentence=50))
print(generate_trigramme('fr', 50))