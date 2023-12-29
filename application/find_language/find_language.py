import requests
import numpy as np

S = requests.Session()

characters_to_remove = [
    '=', '.', ',', '(', ')', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '«', '»', '-', '_', 'ⓐ', '\\', ';', '/', '%'
    ':', '?', '[', ']']

traduction_table = str.maketrans('', '', ''.join(characters_to_remove))


def find_language(request, language_request):

    url = f"https://{language_request}.wikipedia.org/w/api.php"
    data = []
    params = {
        "action": "query",
        "format": "json",
        "titles": request,
        "prop": "extracts",
        "explaintext": True
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        page_content = list(data["query"]["pages"].values())[0]["extract"]
        page_content = [word for word in page_content.split()]
        data = [chaine.translate(traduction_table).lower()
                    for chaine in page_content]
        data = [''.join([c for c in word if ord(c) < 255]) 
                            for word in data]
        data = list(filter(lambda x: x != '', data))
    else:
        print("La requête a échoué. Statut :", response.status_code)

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


print(find_language("Football", 'en'))