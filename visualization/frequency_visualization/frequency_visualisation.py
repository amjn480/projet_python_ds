import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def frequency_visualization(language):
    """Provide a visualization of frequencies."""
    # Loading of the file
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
    # Save the plot
    plt.savefig(f'/home/onyxia/work/projet_python_ds/visualization/frequency_visualization/frequencies_{language}.png')


def worcloud_visualization(language):
    """Provide another visualization of frequencies."""
    # Load of the frequencies
    frequencies = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
    freq = {chr(n): frequencies[n] for n in range(255)}
    wordcloud = WordCloud(width=800, height=400, background_color='white', prefer_horizontal=1.0).generate_from_frequencies(freq)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    plt.savefig(f'/home/onyxia/work/projet_python_ds/visualization/frequency_visualization/wordcloud_{language}.png')


def frequency_visualization_zoom(language):
    """Provide a zoom of the first visualization of frequencies."""
    frequencies = np.loadtxt(f"/home/onyxia/work/projet_python_ds/training/Frequency/Frequencies_{language}.txt")
    frequencies=frequencies[np.ix_([32] + list(range(97, 123)) + list(range(224, 255)))]
    colors = plt.cm.Blues(frequencies)
    plt.figure(figsize=(58, 50))
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
    plt.savefig(f'/home/onyxia/work/projet_python_ds/visualization/frequency_visualization/frequencies_zoom_{language}.png')


# To save the different matrix
for language in ['fr', 'en', 'es', 'de', 'nl', 'it', 'af', 'ca', 'pl', 'sv']:
    #frequency_visualization(language=language)
    #worcloud_visualization(language=language)
    frequency_visualization_zoom(language=language)