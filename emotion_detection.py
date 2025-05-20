from deepface import DeepFace

def detect_emotion(image_path):
    """
    Detect dominant emotion from an image using DeepFace.
    """
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=True)
        analysis = result[0] if isinstance(result, list) else result
        dominant_emotion = analysis['dominant_emotion']
        # DeepFace emotions are lowercase; normalize to capitalized form for mapping
        return dominant_emotion.capitalize()
    except Exception as e:
        print("Error detecting emotion:", e)
        return None
