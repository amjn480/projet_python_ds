import requests
import pickle
import conf
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(path_script))

# Retrieve the first titles of Wikipedia articles for each letter in each language.

S = requests.Session()

language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]

for language in language_list:
    URL = f"https://{language}.wikipedia.org/w/api.php"
    data = []
    for letter in range(ord("A"), ord("Z")+1):
        PARAMS = {
            "action": "opensearch",
            "namespace": "0",
            "search": chr(letter),
            "limit": "15",
            "format": "json"
        }

        response = S.get(url=URL, params=PARAMS)
        data += response.json()[1]
    file = open(path_root + f"/data/list_{language}.pickle", "wb")
    pickle.dump(data, file)
    file.close()
