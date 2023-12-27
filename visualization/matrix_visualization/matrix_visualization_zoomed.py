import numpy as np
import os
import json

import conf_training
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

for language in conf_training.dic_api.keys():

    matrix = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Matrix/Matrix_{language}.txt")
    
    rows_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    cols_to_keep = np.array([32] + list(range(97, 123)) + list(range(224, 255)))
    submatrix = matrix[np.ix_(rows_to_keep,cols_to_keep)].copy()
    submatrix=(submatrix.astype('float'))**0.25
    submatrix[submatrix>1]=1
    

    # Affichage des couleurs représentant les fréquences
    plt.figure(figsize=(15, 15))
    plt.imshow(matrix, interpolation='nearest', cmap='BuPu')
    plt.axis('off')


    for ip,i in enumerate(list(range(0,256))):
        plt.text(-1,ip,chr(i), horizontalalignment='center', verticalalignment='center')
        plt.text(ip,-1,chr(i), horizontalalignment='center', verticalalignment='center')
    plt.colorbar()
    plt.savefig(f"/home/onyxia/work/projet_python_ds/visualization/matrix_visualization/Matrix_viz_{language}_zoomed.png")