import numpy as np
import os


# def encoding(c):
# #cette fonction permettra de convertir un caractère ASCII en un entier
#     return None


class bigram():
    def __init__(self, number_char, language):
        self.language = language
        self.nb = number_char
        self.matrix = np.zeros((number_char, number_char))
        self.total = np.zeros(number_char)
        self.list_articles = os.listdir(f"data/{language}")

    def matrix_transition(self, language, file):
        with open(f"data/{language}/{file}.txt", 'r') as data:
            for word in data:
                for k in range(len(word)-1):
                    character = word[k]
                    next_character = word[k+1]
                    i = encoding(character)
                    j = encoding(next_character)
                    self.matrix[i][j] += 1
                    self.total[i]+=1
                self.matrix[encoding[word[-1]]]
        
        f.close()
    # on fait tourner sur tous les textes pour une langue
    def proba(language , number_char ) :
        URL = f"https://{language}.wikipedia.org/w/api.php"
        data = []
        for letter in range(ord("A"), ord("Z")+1):
            PARAMS = {
                "action": "opensearch",
                "namespace": "0",
                "search": chr(letter),
                "limit": "15",
                "format": "json"
            }

            response = S.get(url=URL, params=PARAMS)
            data += response.json()[1]
        classe=bigram(number_char, language)
        for elmt in data :
            classe.matrix_transition(elmt)
        proba=classe.matrix
        total=classe.total
        #il faudra diviser les probas par total pour avoir bien une matrice de transition et voir comment on calcule les epsilon


language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]
list_matrix=[]
for language in language_list :
    list_matrix.append(proba(language, number_char))