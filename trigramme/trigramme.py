import numpy as np
import os
import json

code_space = 0



class Trigramme():
    def __init__(self, language):
        self.language = language
        self.matrix = np.zeros((255**2, 255**2))
        self.total = np.zeros(255**2)
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
                for word in data:
                    print(word)
                    self.matrix[32][ord(word[0])] += 1 #a changer c faux
                    self.total[32] += 1
                    for k in range(len(word)-3):
                        bicar = word[k:(k+2)]
                        print(bicar)
                        i = Trigramme.encoding(bicar)
                        j = Trigramme.encoding(word[k+1:k+3])
                        self.matrix[i][j] += 1
                        self.total[i] += 1                    
                    print(word[-1])
                    print(word)
                    self.matrix[Trigramme.encoding(word[-2:]), Trigramme.encoding(word[-1])] += 1
            except json.decoder.JSONDecodeError:
                print(f"error collecting the data :{file}")

    def train(self):
        for file in self.list_articles:
            self.update_matrix(file=file)
    
    def normalize(self):
        for k in range(255):
            if self.total[k] != 0:
                self.matrix[k] = self.matrix[k]/self.total[k]