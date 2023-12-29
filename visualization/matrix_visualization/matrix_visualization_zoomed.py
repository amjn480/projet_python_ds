import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# For all languages
for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    # Load the matrix
    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
    #We select the rows ans columns with lowercases letters with and wihtout accents
    rows_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    cols_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    submatrix = matrix[np.ix_(rows_to_keep, cols_to_keep)].copy()
    submatrix = (submatrix.astype('float'))**0.25
    
    # Displaying colors representing frequencies.
    plt.figure(figsize=(15, 15))
    plt.imshow(submatrix, interpolation='nearest', cmap='BuPu')
    plt.axis('off')
    plt.title("Affichage de la matrice de transition", fontsize=16, y=1.10)

    for ip, i in enumerate([32] + list(range(97, 123)) + list(range(224, 255))):
        plt.text(-1, ip, chr(i), horizontalalignment='center', verticalalignment='center')
        plt.text(ip, -1, chr(i), horizontalalignment='center', verticalalignment='center')
    plt.colorbar()
    # Save the plot
    plt.savefig(f"/home/onyxia/work/projet_python_ds/visualization/matrix_visualization/Matrix_viz_{language}_zoomed.png")