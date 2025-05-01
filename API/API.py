import requests
import os
from tinytag import TinyTag

class API:
    def __init__(self, file):
        def use_API(title, artist, album, duration):
            url = "https://lrclib.net/api/search"
            params = {
                'track_name': title,
                'artist_name': artist,
                'album_name': album,
                'duration': duration
            }
            r = requests.get(url, params=params)

            if r.status_code == 200:
                data = r.json()

                # Parcourir les résultats pour trouver les paroles
                for item in data:
                    if "syncedLyrics" in item and item["syncedLyrics"]:
                        return item["syncedLyrics"]
                    elif "plainLyrics" in item and item["plainLyrics"]:
                        return item["plainLyrics"]
                return "Aucunes paroles trouvées"
            else:
                return r.status_code
                
        try:
            # Vérifier si un fichier .lrc existe déjà
            directory = os.path.dirname(file)
            lrc_file = os.path.join(directory, f"{os.path.splitext(os.path.basename(file))[0]}.lrc")
            if os.path.exists(lrc_file):
                return

            # Obtenir les métadonnées du fichier musical
            tag = TinyTag.get(file)
            title = tag.title
            artist = tag.artist
            album = tag.album
            duration = tag.duration

            # Obtenir les paroles
            lyrics = use_API(title, artist, album, duration)

            # Enregistrer les paroles dans le fichier LRC
            with open(lrc_file, 'w') as lrc_file:
                lrc_file.write(lyrics)

            print(f"Paroles enregistrées dans {lrc_file}")
        except Exception as e:
            print(f"Erreur lors du traitement du fichier {file}: {e}")

