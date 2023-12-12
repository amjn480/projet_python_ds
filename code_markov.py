import numpy as np
import os

code_space = 0

def encoding(c):
    '''This function encodes an ASCII character'''
    return None


class Matrix():
    def __init__(self, number_char, language):
        self.language = language
        self.nb = number_char
        self.matrix = np.zeros((number_char, number_char))
        self.total = np.zeros(number_char)
        self.list_articles = os.listdir(f"data/{language}")

    def update_matrix(self, language, file):
        with open(f"data/{language}/{file}.txt", 'r') as data:
            for word in data:
                for k in range(len(word)-1):
                    character = word[k]
                    next_character = word[k+1]
                    i = encoding(character)
                    j = encoding(next_character)
                    self.matrix[i][j] += 1
                    self.total[i] += 1
                self.matrix[encoding[word[-1]], code_space] += 1

    def train(self):
        for file in self.list_articles:
            self.update_matrix(language=language, file=file)


        #il faudra diviser les probas par total pour avoir bien une matrice de transition et voir comment on calcule les epsilon


language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]
list_matrix=[]
for language in language_list :
    list_matrix.append(proba(language, number_char))