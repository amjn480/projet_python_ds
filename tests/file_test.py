import json
import numpy as np
import matplotlib.pyplot as plt
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(path_script))


def function_language_detected(data):
    unigram = {language : compute_distance_frequency(np.loadtxt(path_root + f"/training/Frequency/Frequencies_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
    bigram = {language : compute_proba(np.loadtxt(path_root + f"/training/Matrix/Matrix_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
    trigram = {language : compute_proba_tri(np.loadtxt(path_root + f"/training/Matrix/Matrix_Trigramme_{language}.txt"), data) for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
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
    frequencies_text = np.zeros(256)
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

unigram = {language: [0, 0] for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
bigram = {language: [0, 0] for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}
trigram = {language: [0, 0] for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']}

# for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
#     for file in os.listdir(f"/home/onyxia/work/projet_python_ds/tests/data_test/articles_test/{language}"):
#         print(file)
#         with open(f"/home/onyxia/work/projet_python_ds/tests/data_test/articles_test/{language}/{file}", 'r') as file2:
#             try:
#                 data = json.load(file2)
#                 language_detected = function_language_detected(data=data)
#                 print(language_detected)
#                 if language_detected[0] == language:
#                     unigram[language][0] += 1
#                 unigram[language][1] += 1
#                 if language_detected[1] == language:
#                     bigram[language][0] += 1
#                 bigram[language][1] += 1
#                 if language_detected[2] == language:
#                     trigram[language][0] += 1
#                 trigram[language][1] += 1
#             except (json.decoder.JSONDecodeError, UnicodeDecodeError):
#                 print(f'error collecting the data : {file}')

unigram = {'fr': [103, 104], 'en': [104, 104], 'es': [104, 104], 'de': [104, 104],'nl': [98, 101],'it': [103, 104],'af': [101, 104],'ca': [103, 104],'pl': [104, 104],'sv': [104, 104]}
bigram = {'fr': [104, 104], 'en': [74, 104], 'es': [104, 104], 'de': [77, 104],'nl': [86, 101],'it': [104, 104],'af': [75, 104],'ca': [78, 104],'pl': [102, 104],'sv': [43, 104]}
trigram = {'fr': [103, 104], 'en': [104, 104], 'es': [103, 104], 'de': [103, 104],'nl': [99, 101],'it': [104, 104],'af': [102, 104],'ca': [103, 104],'pl': [100, 104],'sv': [103, 104]}

for ngram in [unigram, bigram, trigram]:
    languages = ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']
    success = [ngram[language][0] for language in languages]
    total = [ngram[language][1] for language in languages]
    frequencies = [r_succes / r_total for r_succes, r_total in zip(success, total)]

    plt.figure(figsize=(10, 6))
    plt.bar(languages, frequencies, color='skyblue')
    plt.title('Pourcentage of good detection')
    plt.xlabel('Languages')
    plt.ylabel('Pourcentage')
    plt.ylim(0, 1)  # The y axis is between 0 and 100
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path_root + f'/tests/results/{ngram}_test.png')

