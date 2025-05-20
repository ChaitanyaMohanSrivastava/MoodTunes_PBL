import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Use your environment variables or hardcoded credentials here
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="23868d32d91e4ea88056ef8716b4a8bb",
    client_secret="dc5b1cca75ed410da0f8e15401d3bcee"
))

def get_music_recommendations(emotion):
    mood_to_genre = {
        "Happy": "pop",
        "Sad": "acoustic",
        "Angry": "rock",
        "Surprise": "dance",
        "Fear": "ambient",
        "Disgust": "metal",
        "Neutral": "chill",
        "Relaxed": "chill"
    }
    genre = mood_to_genre.get(emotion, "pop")
    offset = random.randint(0, 50)  # Reduced to avoid out of range
    results = sp.search(q=f"genre:{genre}", type="track", limit=10, offset=offset)

    songs = []
    for track in results['tracks']['items']:
        songs.append({
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify'],
            "image_url": track['album']['images'][0]['url']
        })
    return songs
