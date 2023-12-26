import numpy as np
import matplotlib.pyplot as plt


def frequency_visualization(language):
    frequencies = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
    colors = plt.cm.Blues(frequencies)
    plt.figure(figsize=(255, 10))
    for i, freq in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=freq)
        plt.text(i + 0.5, 1.1, chr(i), ha='center', fontsize=8)

    plt.title('Exemple de fréquences des caractères ASCII')
    plt.xlabel('Caractères ASCII')
    plt.ylabel('Fréquence')

    plt.xlim(0, len(frequencies))
    plt.ylim(0, 1)
    plt.axis('off')  # Masquer les axes

    plt.show()
    plt.savefig(f'/home/onyxia/work/projet_python_ds/visualization/frequency_visualization/frequencies_{language}.png')


# To save the different matrix
for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    frequency_visualization(language=language)