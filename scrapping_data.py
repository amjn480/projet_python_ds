import requests
import pickle
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

S = requests.Session()

country_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af"]

for elt in country_list:
    URL = f"https://{elt}.wikipedia.org/w/api.php"
    data = []
    for lettre in range(ord("A"), ord("Z")+1):
        PARAMS = {
            "action": "opensearch",
            "namespace": "0",
            "search": chr(lettre),  
            "limit": "15",
            "format": "json"
        }

        R = S.get(url=URL, params=PARAMS)
        data += R.json()[1]
    file = open(f"list_of_wikiarticle/list_{elt}.pickle", "wb")
    pickle.dump(data, file)
    file.close()


