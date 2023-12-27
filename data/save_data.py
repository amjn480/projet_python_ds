import requests
import pickle
import json
import conf_data
import re


def main():
    for language in conf_data.dic_api.keys():
        file = open(
            f"/home/onyxia/work/projet_python_ds/data/list_{language}.pickle",
            "rb")
        requests_list = pickle.load(file)
        for request in requests_list:
            params = {
                "action": "query",
                "format": "json",
                "titles": request,
                "prop": "extracts",
                "explaintext": True}
            headers = {"Accept-Charset": "utf-8"}
            response = requests.get(conf_data.dic_api[language], params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                data = list(data["query"]["pages"].values())[0]["extract"]
                data = data.lower()
                data = data.replace("\n", "")
                data = re.sub(r'=+', "", data)
            else:
                print("La requête a échoué. Statut :", response.status_code)
            try:  # error if there is a backslash in the request
                with open(
                    f"/home/onyxia/work/projet_python_ds/data/{language}/{request}.txt", "w",
                    encoding="utf-8") as file2:
                    file2.write(data)
            except FileNotFoundError:
                print(f"problem for the request: {request}")


if __name__ == '__main__':
    main()