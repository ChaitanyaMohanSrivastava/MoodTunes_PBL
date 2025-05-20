from flask import Flask, request, render_template
from emotion_detection import detect_emotion
from music_recommender import get_music_recommendations
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            image_path = os.path.join("uploads", file.filename)
            os.makedirs("uploads", exist_ok=True)
            file.save(image_path)
            emotion = detect_emotion(image_path)
        else:
            emotion = None
    else:
        # Optional fallback if you want to allow manual input
        emotion = request.form.get('emotion')

    if not emotion:
        emotion = "Neutral"  # Default emotion fallback

    songs = get_music_recommendations(emotion)
    return render_template('results.html', emotion=emotion, songs=songs)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
