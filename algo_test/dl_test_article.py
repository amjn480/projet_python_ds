import requests
import pickle
import conf

S = requests.Session()

language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]

for language in language_list:
    with open(f"/home/onyxia/work/projet_python_ds/data/wikipedia_articles/list_{language}.pickle", "rb") as f:
        training_data = pickle.load(f)
    URL = f"https://{language}.wikipedia.org/w/api.php"
    data = []
    for letter in range(ord("A"), ord("Z")+1):
        PARAMS = {
            "action": "opensearch",
            "namespace": "0",
            "search": chr(letter),
            "limit": "30",
            "format": "json"
        }

        response = S.get(url=URL, params=PARAMS)
        for elt in response.json()[1]:
            if elt not in training_data:
                data += [elt]
                break
    file = open(f"/home/onyxia/work/projet_python_ds/algo_test/article_title/list_{language}_test.pickle", "wb")
    pickle.dump(data, file)
    file.close()