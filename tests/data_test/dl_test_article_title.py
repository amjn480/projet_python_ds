import requests
import pickle
import os

path_script = os.path.abspath(__file__)

path_root = os.path.dirname(os.path.dirname(os.path.dirname(path_script)))

S = requests.Session()

language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]

for language in language_list:
    with open(path_root + f"/data/wikipedia_articles/list_{language}.pickle", "rb") as f:
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
        count = 0
        for elt in response.json()[1]:
            if elt not in training_data and count < 4:
                data += [elt]
                count += 1
    file = open(path_root + f"/tests/data_test/article_title_test/list_{language}_test.pickle", "wb")
    pickle.dump(data, file)
    file.close()