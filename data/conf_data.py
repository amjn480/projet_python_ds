# choix des charactères que l'on garde dans les données récupérées
characters_to_remove = [
    '=', '.', ',', '(', ')', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '«', '»', '-', '_', 'ⓐ', '\\', ';', '/', '%'
    ':', '?']

traduction_table = str.maketrans('', '', ''.join(characters_to_remove))

# The type to encode the data from Wikipedia
encoding_type = 'utf-8'