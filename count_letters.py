import os
import json

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(path_script)

language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]
for elt in language_list:
    path_list = os.listdir(path_root + f"/data/{elt}")
    total_char = 0
    for file in path_list:
        with open(path_root + f"/data/{elt}/" + file, 'r', encoding='utf-8') as article:
            try:
                article = json.load(article)
                for word in article:
                    total_char += (1 + len(word))
            except:
                pass
    print(elt, total_char, "\n")