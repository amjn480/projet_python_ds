import numpy as np
import json
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(os.path.dirname(path_script)))

def code(c):
    if ord(c) == 32:
        enc1 = 0
    elif ord(c) <= 122 and ord(c) >= 97:
        enc1 = ord(c)-96
    elif ord(c) <= 255 and ord(c) >= 224:
        enc1 = ord(c)-197
    else:
        enc1 = 59
    return enc1


class Trigramme():
    def __init__(self, language):
        self.language = language
        self.matrix = np.zeros((60**2, 60**2))
        self.total = np.zeros(60**2)
        self.list_articles = os.listdir(path_root + f"/data/{language}")
        self.train()
        self.normalize()

    @staticmethod
    def encoding(c):
        enc1 = code(c[0])
        enc2 = code(c[1])
        return enc1 + enc2*60

    def update_matrix(self, file):
        with open(path_root + f"/data/{self.language}/{file}", 'r', encoding='utf-8') as file2:
            try:
                data = json.load(file2)
                data = ' '.join(data)
                for k in range(len(data)-3):
                    prev = Trigramme.encoding(data[k:k+2])
                    next = Trigramme.encoding(data[k+1:k+3])
                    self.matrix[prev][next] += 1
                    self.total[prev] += 1             
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f"error collecting the data :{file}")
            
    def train(self):
        for file in self.list_articles:
            self.update_matrix(file=file)
    
    def normalize(self):
        for k in range(60**2):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]


for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    np.savetxt(path_root + f"/training/Matrix/Matrix_Trigramme_{language}.txt", Trigramme(language=language).matrix)
