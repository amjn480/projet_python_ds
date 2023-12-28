# Selection of characters to be retained in the retrieved data.
characters_to_remove = [
    '=', '.', ',', '(', ')', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '«', '»', '-', '_', 'ⓐ', '\\', ';', '/', '%'
    ':', '?', '[', ']']

traduction_table = str.maketrans('', '', ''.join(characters_to_remove))

# The type to encode the data from Wikipedia
encoding_type = 'utf-8'

# The different languages we are going to train the model
dic_api = {
            "fr": "https://fr.wikipedia.org/w/api.php",
            "en": "https://en.wikipedia.org/w/api.php",
            "es": "https://es.wikipedia.org/w/api.php",
            "de": "https://de.wikipedia.org/w/api.php",
            "nl": "https://nl.wikipedia.org/w/api.php",
            "it": "https://it.wikipedia.org/w/api.php",
            "af": "https://af.wikipedia.org/w/api.php",
            "ca": "https://ca.wikipedia.org/w/api.php",
            "pl": "https://pl.wikipedia.org/w/api.php",
            "sv": "https://sv.wikipedia.org/w/api.php"
            }