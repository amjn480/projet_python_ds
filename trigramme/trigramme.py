import numpy as np
import os
import json
import conf_training
code_space = 0


def code(c):
    """Encodes the chain of character 
    Parameters :
    c is a character """
    if ord(c) == 32: # It corresponds to space 
        enc1 = 0 # Space is encoded by 0 in the transition matrix
    elif ord(c) <= 122 and ord(c) >= 97: # It corresponds to  lowercases letters
        enc1 = ord(c)-96 # It is encoded in position 1 to 27 in the matrix 
    elif ord(c) <= 255 and ord(c) >= 224: # It corresponds to lowercases letters with accents
        enc1 = ord(c)-197 # It is encoded in position 28 to 58
    else: # If it is another character, we choose to skip it for trigrams
        enc1 = 59 # Others characters are encoded by 59
    return enc1


class Trigramme():
    def __init__(self, language):
        """Initilizes all the parameters, trains and normalizes the transition matrix for trigrams then"""
        self.language = language
        self.matrix = np.zeros((60**2, 60**2))
        self.total = np.zeros(60**2)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
        self.normalize()

    @staticmethod
    def encoding(c):
        """Encode two characters and return a number in base 60 to associate to each trigram a
        unique number between 0 and 3599 """
        enc1 = code(c[0])
        enc2 = code(c[1])
        return enc1 + enc2*60

    def update_matrix(self, file):
        """Update the matrix by training it on a new file"""
        # Open the file
        with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r', encoding='utf-8') as file2:
            try:
                data = json.load(file2)
                data = ' '.join(data)
                # Update the variables by reading it
                for k in range(len(data)-3):
                    prev = Trigramme.encoding(data[k:k+2])
                    next = Trigramme.encoding(data[k+1:k+3])
                    self.matrix[prev][next] += 1
                    self.total[prev] += 1             
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f"error collecting the data :{file}")
            
    def train(self):
        """Update the matrix by reading all the files"""
        for file in self.list_articles:
            self.update_matrix(file=file)
    
    def normalize(self):
        """Normalize the matrix to have a transition matrix"""
        for k in range(60**2):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]

# Save the matrix for each language
for language in conf_training.dic_api.keys():
    np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_Trigramme_{language}.txt", Trigramme(language=language).matrix)
