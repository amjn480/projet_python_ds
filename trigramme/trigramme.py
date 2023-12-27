import numpy as np
import os
import json
import conf_training
code_space = 0


class Trigramme():
    def __init__(self, language):
        self.language = language
        self.matrix = np.zeros((256**2, 256**2))
        self.total = np.zeros(256**2)
        self.list_articles = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{language}")
        self.train()
        self.normalize()

    @staticmethod
    def encoding(c):
        return ord(c[0])+ord(c[1])*256

    def update_matrix(self, file):
        with open(f"/home/onyxia/work/projet_python_ds/data/{self.language}/{file}", 'r', encoding='utf-8') as file2:
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
        for k in range(256**2):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]


for language in conf_training.dic_api.keys():
    rows_to_keep = np.array([32] + list(range(97, 123))+list(range(224, 255)))
    cols_to_keep = np.array([32] + list(range(97, 123))+list(range(224, 255)))
    np.savetxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_trigramme_{language}.txt", Trigramme(language=language).matrix[np.ix_(rows_to_keep,cols_to_keep)])
