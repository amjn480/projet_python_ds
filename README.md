# Projet pyhton pour la datascience
Voici notre projet de pyhton pour la datascience

Le code se classe en 5 dossiers : algo_test, application, data, training, visualization.

## Dossier data
Le dossier data comporte les données que nous avons scrappé sur Wikipédia pour les dix langues considérées.
Le fichier "scrapping_data.py" enregistre pour les différentes langues, des titres d'articles wikipédia dans le dossier "Wikipedia_articles".
Ensuite, le fichier "save_data.py" enregistre le contenu des requêtes wikipédia pour chaque langue. Les données sont enregistrées de telle sorte à ne garder que les lettres en minuscule, sans chiffres, sans ponctuation.

## Dossier Training
Le dossier training consiste à utiliser les données enregistrées dans le dossier data pour calculer les matrices de transitions pour les chaînes de Markov. Nous avons des sous-dossiers correspondants aux modèles que nous avons utilisé: unigram, bigram, trigram.

Dans ces sous-dossiers, nous retrouvons fichier python permettant de générer les différentes matrices et listes de fréquences. Celles-ci sont ensuite enregistrées dans les sous-dossiers 'Matrix' et 'Frequency'.

## Dossier Visualization
Le dossier visualization veut représenter les matrices et listes de fréquences calculées dans le dossier training. 
Nous retrouvons dans les sous-dossiers les fichiers pythons pour générer les graphiques.

## Dossier application
Le dossier application utilise les données calculées dans le dossier training pour détecter la langue d'un texte inconnu, pour générer des phrases dans une langue.

## Dossier tests
Ce dossier veut tester la performance des différents modèles pour la détecction de langues. 
Nous utilisons des textes provenant de fichiers wikipédia tirés aléatoirement dans chaque langue pour vérifier si les modèles reconnaissent les langues utilisées. 
