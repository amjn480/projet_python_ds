import math
import numpy as np
import random

eps = 1e-6


def generate_bigramme(language, lenght_sentence):
    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
    freq = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")

    current_state = random.choices(range(len(matrix)), weights=freq)[0]
    generated_text = chr(current_state)

    for _ in range(1, lenght_sentence):
        next_state = random.choices(range(len(matrix)), weights=matrix[current_state])[0]
        generated_text += chr(next_state)
        current_state = next_state

    return generated_text


def generate_trigramme(language, lenght_sentence):
    matrix2 = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_Trigramme_{language}.txt")
    freq = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
    rows_to_keep = np.array([32] + list(range(97, 123))+list(range(224, 255)))
    freq = freq[np.ix_(rows_to_keep)]

    current_state2 = random.choices(range(len(freq)), weights=freq)[0]

    while current_state2 == -1:
        current_state2 = random.choices(range(60), weights=freq)[0]   
    current_state = current_state2*60
    print(current_state, "current_state")
    generated_text = decode(current_state)

    for _ in range(1, lenght_sentence):  
        nb = random.choices(range(len(matrix2)), weights=matrix2[current_state])[0]  
        nb1 = nb % 60
        nb2 = nb//60
        while revient(nb2) == -1:
            nb = random.choices(range(len(matrix2)), weights=matrix2[current_state])[0]
            nb2 = nb//60
            nb1 = nb % 60
        next_state = nb  
        
        generated_text += decode(next_state)[1]
        current_state2 = nb2
        current_state = nb
    return generated_text


def perplexity(text, language):
    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
    res = 0
    c1 = text[0]
    for c2 in text[1:]:
        i = ord(c1)
        j = ord(c2)
        res += math.log(matrix[i, j] + eps)
        c1 = c2
    return res


def revient(nb):
    """permet de se ramener dans le bon intervalle"""
    if nb == 0:
        return 32
    elif nb <= 26:
        return nb+96
    elif nb <= 58:
        return nb+197
    else:
        return -1


def decode(nb):
    """trouve les nombres en base 10 pour réassocier la chaine de caractere"""
    if nb < 0:
        return -1
    c = ''
    c += chr(revient(nb % 60))
    c += chr(revient(nb//60))
    return c


# To generate sentences with the bigramme model and the trigramme model

print(generate_bigramme(language='fr', lenght_sentence=50))
print(generate_trigramme('fr', 50))