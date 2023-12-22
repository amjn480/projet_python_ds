import numpy as np
import os
import json
import conf_training

code_space = 0


def encoding(c):
    '''This function encodes an ASCII character that'''
    if ord(c) <= 122:
        return ord(c) - 97
    elif 224 <= ord(c):
        return ord(c) - (198)
    elif c == 'space':
        return 58


class Matrix():
    def __init__(self, language):
        self.language = language
        self.matrix = np.zeros((255, 255))
        self.total = np.zeros(255)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
        self.normalize()

    def update_matrix(self, file):
        with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r', encoding='utf-8') as file2:
            try:
                data = json.load(file2)
                for word in data:
                    self.matrix[32][ord(word[0])] += 1
                    self.total[32] += 1
                    for k in range(len(word)-1):
                        character = word[k]
                        next_character = word[k+1]
                        i = ord(character)
                        j = ord(next_character)
                        self.matrix[i][j] += 1
                        self.total[i] += 1
                    self.matrix[ord(word[-1])][32] += 1
            except json.decoder.JSONDecodeError:
                print(f"error collecting the data :{file}")

    def train(self):
        for file in self.list_articles:
            self.update_matrix(file=file)
    
    def normalize(self):
        for k in range(255):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]


# # Pour visualiser la matrice
# for language in conf_training.dic_api.keys():
#     np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt", Matrix(language=language).matrix)


class Frequency():
    def __init__(self, language):
        self.language = language
        self.frequencies = np.zeros(255)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
    
    def train(self):
        number_characters = 0
        for file in self.list_articles:
            with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r') as file2:
                try:
                    data = json.load(file2)
                    for word in data:
                        number_characters += len(word)
                        for letter in word:
                            self.frequencies[ord(letter)] += 1
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    print(f"error collecting the data :{file}")
        self.frequencies = self.frequencies/number_characters


# Pour visualiser les fréquences des lettres par langues
for language in conf_training.dic_api.keys():
    np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Frequencies_{language}.txt", Frequency(language=language).frequencies)
