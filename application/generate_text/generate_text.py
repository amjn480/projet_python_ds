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
    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_trigramme_{language}.txt")
    freq = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")


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


# To generate sentences with the bigramme model and the trigramme model

print(generate_bigramme(language='fr', lenght_sentence=50))