import numpy as np
#au début je prends seulement les caractères de a à z
#pour les 2 grams
def convert_to_int(c):
#cette fonction permettra de convertir un caractère ASCII en un entier
    return None

class bigram :
    def __init__(self, number_char, language):
        self.language=language
        
        self.nb=number_char
        self.matrix=np.zeros((number_char, number_char))
        self.total=np.zeros(number_char)

    def matrix_transition(self, name) :
        #name est le nom du fichier
        #j'ai pas pris en compte les espaces mais faudra rajouter une ligne
        f=open(self.name)
        contenu=eval(f.read())
        
        for mot in contenu :
            i=0
            for c in mot :
                j=convert_to_int(c)
                self.matrix[i,j]+=1
                self.total[i]+=1
                i=j
        
        f.close()
#on fait tourner sur tous les textes pour une langue
def proba(language , number_char ) :
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
    classe=bigram(number_char, language)
    for elmt in data :
        classe.matrix_transition(elmt)
    proba=classe.matrix
    total=classe.total
    #il faudra diviser les probas par total pour avoir bien une matrice de transition et voir comment on calcule les epsilon


language_list = ["en", "pl", "fr", "es", "it", "de", "ca", "sv", "af", "nl"]
list_matrix=[]
for language in language_list :
    list_matrix.append(proba(language, number_char))