import requests
import conf_data
import numpy as np

S = requests.Session()


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
        data = [chaine.translate(conf_data.traduction_table).lower()
                    for chaine in page_content]
        data = [''.join([c for c in word if ord(c) < 255]) 
                            for word in data]
        data = list(filter(lambda x: x != '', data))
    else:
        print("La requête a échoué. Statut :", response.status_code)

    for language in conf_data.dic_api.keys():
        proba = compute_proba(np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt"), data)
        distance = compute_distance_frequency(np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt"), data)
        print(f"The probabilty with the Matrix for {language} is :{proba}")
        print(f"The distance for {language} is : {distance}")


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
                proba = proba*matrix[i][j]
            proba = proba*matrix[ord(word[-1])][32]
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


print(find_language("Football", 'fr'))