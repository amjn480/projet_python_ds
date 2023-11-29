import requests
import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    file = open(f"list_of_wikiarticle/list_{language}.pickle", "wb")
    pickle.dump(data, file)
    file.close()
