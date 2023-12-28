import conf_data
import os
import json
import numpy as np


def function_language_detected(data):
    unigram = {language : compute_distance_frequency(np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
    bigram = {language : compute_proba(np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
    trigram = {language : compute_proba_tri(np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_Trigramme_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
    return (min(unigram, key=unigram.get), max(bigram, key=bigram.get), max(trigram, key=trigram.get))

def compute_proba(matrix, text):
        """text is a list of word"""
        proba_totale = 0
        for word in text:
            proba = 1
            for k in range(len(word)-1):
                character = word[k]
                next_character = word[k+1]
                i = ord(character)
                j = ord(next_character)
                proba = proba*(matrix[i][j])
            proba = proba*(matrix[ord(word[-1])][32])
            proba_totale += proba
        return proba_totale/len(text)


def compute_distance_frequency(frequencies, text):
    frequencies_text = np.zeros(255)
    number_characters = 0
    for word in text:
        number_characters += len(word)
        for letter in word:
            frequencies_text[ord(letter)] += 1
    frequencies_text = frequencies_text/number_characters
    return np.linalg.norm(frequencies - frequencies_text)


def compute_proba_tri(matrix, text):
    text = ' '.join(text)
    proba_totale = 0
    for k in range(len(text)//15):
        proba = 1
        for j in range(15*k, 15*(k + 1) - 3):
            prev = encoding_tri(text[j:j+2])
            next = encoding_tri(text[j+1:j+3])
            proba *= matrix[prev][next]
        proba_totale += proba
    return proba_totale/(len(text)//15)


def encoding_tri(c):
    enc1 = code(c[0])
    enc2 = code(c[1])
    return enc1 + enc2*60


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


# Test for the unigram model

unigram = {language: [0, 0] for language in conf_data.dic_api.keys()}

for language in conf_data.dic_api.keys():
    for file in os.listdir(f"/home/onyxia/work/projet_python_ds/algo_test/articles_test/{language}"):
        with open(f"/home/onyxia/work/projet_python_ds/algo_test/articles_test/{language}/{file}", 'r') as file2:
            try:
                data = json.load(file2)
                language_detected = function_language_detected(data=data)[0]
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
                language_detected = function_language_detected(data=data)[1]
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
                language_detected = function_language_detected(data=data)[2]
                if language_detected == language:
                    trigram[language][0] += 1
                trigram[language][1] += 1
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                print(f'error collecting the data : {file}')