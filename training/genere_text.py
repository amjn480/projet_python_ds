import math
import numpy as np
import random
language='fr'
matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
freq=np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
eps=1e-6


def perplexity(s) :
    res=0
    c1=s[0]
    for c2 in s[1:] :
        i=ord(c1)
        j=ord(c2)
        res+=math.log(matrix[i,j]+eps)
        c1=c2
    return res

def genere_txt(n) :
    current_state = random.choices(range(len(matrix)), weights=freq)[0]    
    generated_text = chr(current_state)

    # Générer le reste du texte en suivant la chaîne de Markov
    for _ in range(1, n):        
        next_state = random.choices(range(len(matrix)), weights=matrix[current_state])[0]        
        print(next_state)
        generated_text+=chr(next_state)
        current_state = next_state

    return generated_text
txt=genere_txt(50)
print(txt)
print(perplexity(txt))