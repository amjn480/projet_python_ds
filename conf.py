# File to configure the different settings
import os

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

# App root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Project root