import requests
import pickle

# URL de l'API de Wikipedia
dic = {"fr": "https://fr.wikipedia.org/w/api.php",
        "en": "https://en.wikipedia.org/w/api.php",
        "es": "https://es.wikipedia.org/w/api.php",
        "de": "https://de.wikipedia.org/w/api.php",
        "nl": "https://nl.wikipedia.org/w/api.php",
        "it": "https://it.wikipedia.org/w/api.php",
        "af": "https://af.wikipedia.org/w/api.php",
        "ca": "https://ca.wikipedia.org/w/api.php",
        "pl": "https://pl.wikipedia.org/w/api.php",
        "sv":"https://sv.wikipedia.org/w/api.php"}


for language in ["pl", "sv"]:
    file = open(f"/home/onyxia/work/projet_python_ds/list_of_wikiarticle/list_{language}.pickle", "rb")
    requests_list = pickle.load(file)
    for request in requests_list:
        params = {
            "action": "query",
            "format": "json",
            "titles": request,
            "prop": "extracts",
            "explaintext": True}
        response = requests.get(dic[language], params=params)
        if response.status_code == 200:
            data = response.json()
            page_content = list(data["query"]["pages"].values())[0]["extract"]
        else:
            print("La requête a échoué. Statut :", response.status_code)
        try:  # if there is a bachslah in the request, the algorithm looks for a directory that doesn't exist
            with open(f"data/{language}/{request}.txt", "w", encoding='utf-8') as file2:
                file2.write(page_content)
        except FileNotFoundError:
            print(f"problem for the request: {request}") 

