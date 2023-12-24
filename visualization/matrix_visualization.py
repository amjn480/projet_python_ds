import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

"""language = "fr"
matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
colors = np.zeros((len(matrix), len(matrix[0]), 3))
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
plt.colorbar()  # Barre de couleur pour référence
plt.show(block=True)
plt.savefig(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_viz_{language}.png")
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use TkAgg for interactive zooming
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    ax.set_xlim(min(x1, x2), max(x1, x2))
    ax.set_ylim(min(y1, y2), max(y1, y2))
    plt.draw()

language = "fr"
matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
colors_hsv = np.zeros((255, 255, 3))

for i in range(255):
    for j in range(255):
        alpha = 0.25
        colors_hsv[i, j, 0] = matrix[i, j] ** alpha

colors_rgb = plt.get_cmap('hsv')(colors_hsv[:, :, 0])

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))

# Display the colors representing frequencies
im = ax.imshow(colors_rgb, interpolation='nearest')

# Set title and labels
ax.set_title('Couleurs en fonction des fréquences')
ax.set_xlabel('Lettre suivante')
ax.set_ylabel('Lettre actuelle')

# Add colorbar for reference
cbar = plt.colorbar(im)

# Enable zooming functionality
rs = RectangleSelector(ax, onselect)

# Display the plot
plt.show()

# Save the plot after interactive features (e.g., zooming) are done
plt.savefig(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_viz_{language}_zoomed.png")