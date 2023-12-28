import conf_data
import os
import json
import numpy as np
import projet_python_ds.application.find_language.find_language

# Test for the unigram model

unigram = {language: [0, 0] for language in conf_data.dic_api.keys()}

for language in conf_data.dic_api.keys():
    for file in os.listdir(f"/home/onyxia/work/projet_python_ds/algo_test/articles_test/{language}"):
        with open(file, 'r') as file2:
            try:
                data = json.load(file2)
                frequencies = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
                language_detected = find_language.compute_distance_frequency(frequencies=frequencies, data=data)
                if language_detected == language:
                    unigram[language][0] += 1
                unigram[language][1] += 1
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f'error collecting the data : {file}')


# Test for the bigram model

bigram = {language: [0, 0] for language in conf_data.dic_api.keys()}

for language in conf_data.dic_api.keys():
    for file in os.listdir(f"/home/onyxia/work/projet_python_ds/algo_test/articles_test/{language}"):
        with open(file, 'r') as file2:
            try:
                data = json.load(file2)
                matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
                language_detected = find_language.compute_proba(matrix=matrix, data=data)
                if language_detected == language:
                    bigram[language][0] += 1
                bigram[language][1] += 1
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f'error collecting the data : {file}')


# Test for the trigram model

trigram = {language: [0, 0] for language in conf_data.dic_api.keys()}

for language in conf_data.dic_api.keys():
    for file in os.listdir(f"/home/onyxia/work/projet_python_ds/algo_test/articles_test/{language}"):
        with open(file, 'r') as file2:
            try:
                data = json.load(file2)
                matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_Trigramme_{language}.txt")
                language_detected = find_language.compute_proba_tri(matrix=matrix, data=data)
                if language_detected == language:
                    trigram[language][0] += 1
                trigram[language][1] += 1
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f'error collecting the data : {file}')