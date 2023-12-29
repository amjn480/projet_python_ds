import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

path_script = os.path.abspath(__file__)
path_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(path_script))))


# For all languages
for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    # Load the matrix
    matrix = np.loadtxt(path_root + f"/training/Matrix/Matrix_{language}.txt")
    #We select the rows ans columns with lowercases letters with and wihtout accents
    rows_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    cols_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    submatrix = matrix[np.ix_(rows_to_keep, cols_to_keep)].copy()
    submatrix = (submatrix.astype('float'))**0.25
    
    # Displaying colors representing frequencies.
    plt.figure(figsize=(15, 15))
    plt.imshow(submatrix, interpolation='nearest', cmap='BuPu')
    plt.axis('off')
    plt.title(f"Affichage de la matrice de transition en {language}", fontsize=16, y=1.10)

    for ip, i in enumerate([32] + list(range(97, 123)) + list(range(224, 255))):
        plt.text(-1, ip, chr(i), horizontalalignment='center', verticalalignment='center')
        plt.text(ip, -1, chr(i), horizontalalignment='center', verticalalignment='center')
    plt.colorbar()
    # Save the plot
    plt.savefig(path_root + f"/visualization/matrix_visualization/Matrix_viz_{language}_zoomed.png")