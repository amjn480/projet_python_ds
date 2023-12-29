import numpy as np
import json


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

