import os
import json

language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]
for elt in language_list:
    path_list = os.listdir(f"/home/onyxia/work/projet_python_ds/data/{elt}")
    total_char = 0
    for file in path_list:
        with open(f"/home/onyxia/work/projet_python_ds/data/{elt}/" + file, 'r', encoding='utf-8') as article:
            try:
                article = json.load(article)
                for word in article:
                    total_char += (1 + len(word))
            except:
                pass
    print(elt, total_char, "\n")