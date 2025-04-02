import requests
import os
from tinytag import TinyTag

# Fichiers audio
dossier = input("Quel répertoire fouiller ? ")

def fichiers_audio():
    for root, dirs, files in os.walk(dossier):
        for file in files:
            if file.endswith(('.mp3', '.flac', '.wav', '.ogg')):
                treat_file(os.path.join(root, file), root)

# API
def paroles(title, artist, album, duration):
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
        return f"Erreur: {r.status_code}"

# Fichier LRC
def treat_file(file, directory):
    try:
        # Vérifier si un fichier .lrc existe déjà
        lrc_filename = os.path.join(directory, f"{os.path.splitext(os.path.basename(file))[0]}.lrc")
        if os.path.exists(lrc_filename):
            print(f"Fichier LRC existant trouvé pour {file}. Passage au fichier suivant.")
            return

        # Obtenir les métadonnées du fichier musical
        tag = TinyTag.get(file)
        track = tag.title
        artist = tag.artist
        album = tag.album
        duration = tag.duration

        # Obtenir les paroles
        lyrics = paroles(track, artist, album, duration)

        # Enregistrer les paroles dans le fichier LRC
        with open(lrc_filename, 'w') as lrc_file:
            lrc_file.write(lyrics)

        print(f"Paroles enregistrées dans {lrc_filename}")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {fichier}: {e}")

# Appel de la fonction principale
fichiers_audio()
