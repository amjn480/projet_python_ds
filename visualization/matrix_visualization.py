import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


language = "fr"
matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
colors = np.zeros((len(matrix), len(matrix[0]), 3))
for i in range(len(matrix)):
    for j in range(len(matrix)):
        colors[i][j] = [matrix[i][j], matrix[i][j], matrix[i][j]]

colors_hsv = np.zeros((255, 255, 3))  # Matrice pour stocker les couleurs en HSV
for i in range(255):
    for j in range(255):
        colors_hsv[i, j, 0] = matrix[i, j]  # Teinte correspondant à la fréquence

# Conversion des couleurs de l'espace HSV à RGB pour l'affichage
colors_rgb = plt.get_cmap('hsv')(colors_hsv[:, :, 0])  # Utilisation uniquement de la teinte pour la colormap

# Affichage des couleurs représentant les fréquences
plt.figure(figsize=(8, 6))
plt.imshow(colors_rgb, interpolation='nearest')
plt.title('Couleurs en fonction des fréquences')
plt.xlabel('Lettre suivante')
plt.ylabel('Lettre actuelle')
plt.colorbar()  # Barre de couleur pour référence
plt.show(block=True)
#plt.savefig(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_viz_{language}.jpeg")
