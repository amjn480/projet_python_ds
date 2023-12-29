import numpy as np
import matplotlib.pyplot as plt


def matrix_visualiation(language):
    """Save a visualization of transition matrices"""
    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
    colors = np.zeros((len(matrix), len(matrix[0]), 3))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            colors[i][j] = [matrix[i][j], matrix[i][j], matrix[i][j]]

    colors_hsv = np.zeros((256, 256, 3))  # Matrix to store colors in HSV (Hue, Saturation, Value).
    for i in range(256):
        for j in range(256):
            colors_hsv[i, j, 0] = matrix[i, j]  # Hue corresponding to frequency

    # Conversion of colors from HSV space to RGB for display
    colors_rgb = plt.get_cmap('Blues')(colors_hsv[:, :, 0])  # Utilisation uniquement de la teinte pour la colormap

    plt.figure(figsize=(8, 6))
    plt.imshow(colors_rgb, interpolation='nearest', cmap='Blues')
    plt.title('Couleurs en fonction des fréquences')
    plt.xlabel('Lettre suivante')
    plt.ylabel('Lettre actuelle')

    cbar = plt.colorbar()
    cbar.set_label("Valeur des fréquences")

    plt.show()
    plt.savefig(f'/home/onyxia/work/projet_python_ds/visualization/matrix_visualization/matrix_{language}.png')


# To save the different matrix
for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    matrix_visualiation(language=language)