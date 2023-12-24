import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt










language = "fr"
matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
rows_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
cols_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))

# Use advanced indexing to keep the desired portion
submatrix = matrix[np.ix_(rows_to_keep,cols_to_keep)] .copy()
submatrix=(submatrix.astype('float'))**0.5
submatrix[submatrix>1]=1
"""colors = np.zeros((len(matrix), len(matrix[0]), 3))
for i in range(len(matrix)):
    for j in range(len(matrix)):
        colors[i][j] = [matrix[i][j], matrix[i][j], matrix[i][j]]

colors_hsv = np.zeros((255, 255, 3))  # Matrice pour stocker les couleurs en HSV
for i in range(255):
    for j in range(255):
        alpha=0.25
        colors_hsv[i, j, 0] = matrix[i, j]**alpha  # Teinte correspondant à la fréquence

# Conversion des couleurs de l'espace HSV à RGB pour l'affichage
colors_rgb = plt.get_cmap('hsv')(colors_hsv[:, :, 0])  # Utilisation uniquement de la teinte pour la colormap

# Affichage des couleurs représentant les fréquences
plt.figure(figsize=(8, 6))
plt.imshow(colors_rgb, interpolation='nearest')
plt.title('Couleurs en fonction des fréquences')
plt.xlabel('Lettre suivante')
plt.ylabel('Lettre actuelle')
plt.colorbar() """






# Affichage des couleurs représentant les fréquences
plt.figure(figsize=(15, 15))
plt.imshow(submatrix, interpolation='nearest', cmap='BuPu')
plt.axis('off')


for ip,i in enumerate([32]+list(range(97,123))+list(range(224,255))):
    plt.text(-1,ip,chr(i), horizontalalignment='center', verticalalignment='center')
    plt.text(ip,-1,chr(i), horizontalalignment='center', verticalalignment='center')
plt.colorbar()
plt.savefig(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_viz_{language}_zoomed.png")

