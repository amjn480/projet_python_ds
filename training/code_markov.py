import numpy as np
import os
import json
import conf_training

code_space = 0


def encoding(c):
    '''This function encodes an ASCII character'''
    # If ord(c)<=122, letters are lowercases letters
    if ord(c) <= 122:
        return ord(c) - 97
    # If 224<=ord(c), letters correspond to lowercases with accents
    elif 224 <= ord(c):
        return ord(c) - (198)
    elif c == 'space':
        return 58


class Matrix():
    def __init__(self, language):
        """Initializes all the parameters"""
        self.language = language
        # Matrix represents the transition matrix of Markov chain
        self.matrix = np.zeros((255, 255))
        # Total[i] counts the nummber of transitions whose first letter is i for all i
        self.total = np.zeros(255)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
        self.normalize()

    def update_matrix(self, file):
        """ Update matrix of a language by training it with a new file""" 
        # Open the file
        with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r', encoding='utf-8') as file2:
            try:
                data = json.load(file2)
                # Read the file
                for word in data:
                    # Update variables
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
                    self.total[ord(word[-1])] += 1
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f"error collecting the data :{file}")

    def train(self):
        """Update the matrix with all the files of a language"""
        for file in self.list_articles:
            self.update_matrix(file=file)
    
    def normalize(self):
        """Normalize the matrix"""
        for k in range(255):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]


# To save the matrix in a file
# for language in conf_training.dic_api.keys():
#     np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt", Matrix(language=language).matrix)


class Frequency():
    def __init__(self, language):
        """Initializes all the parameters"""
        self.language = language
        self.frequencies = np.zeros(255)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
    
    def train(self):
        """ Trains the array of frequencies with the files for a language"""
        number_characters = 0
        #We read all the files
        for file in self.list_articles:
            # We open a file
            with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r') as file2:
                try:
                    data = json.load(file2)
                    # We read a file
                    for word in data:
                        #We update variables
                        number_characters += len(word)
                        for letter in word:
                            self.frequencies[ord(letter)] += 1
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    print(f"error collecting the data :{file}")
        self.frequencies = self.frequencies/number_characters


# To save the list in a file
# for language in conf_training.dic_api.keys():
#     np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt", Frequency(language=language).frequencies)

