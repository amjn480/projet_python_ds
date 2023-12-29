import requests
import pickle
import json
import conf_data
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(path_script))


def main():
    '''Scrapes and saves Wikipedia chosen articles into a text file for each language.'''
    for language in conf_data.dic_api.keys():
        file = open(path_root + 
            f"/data/wikipedia_articles/list_{language}.pickle",
            "rb")
        requests_list = pickle.load(file)
        for request in requests_list:
            params = {
                "action": "query",
                "format": "json",
                "titles": request,
                "prop": "extracts",
                "explaintext": True}
            response = requests.get(conf_data.dic_api[language], params=params)
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
            try:  # error if there is a backslash in the request
                with open(path_root + 
                    f"/data/{language}/{request}.txt", "w",
                    encoding=conf_data.encoding_type) as file2:
                    json.dump(data, file2)
            except FileNotFoundError:
                print(f"problem for the request: {request}")


if __name__ == '__main__':
    main()