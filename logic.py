# logic.py - The Intelligent Study Assistant
def get_study_advice(emotion):
    emotion = str(emotion).lower()
    
    # Core Logic from MoodMirror.pdf
    if emotion in ["sad", "angry", "fearful"]:
        status = "⚠️ FATIGUE DETECTED"
        advice = "Take a 15-minute break. Try a quick walk or listening to lo-fi music."
    elif emotion == "happy":
        status = "🚀 FLOW STATE"
        advice = "You are in a great mood! This is the perfect time for complex topics."
    elif emotion == "surprised":
        status = "💡 HIGH ENGAGEMENT"
        advice = "Curiosity detected! Take detailed notes on this section."
    else:
        status = "✅ STEADY PROGRESS"
        advice = "Maintain this pace. Remember to stay hydrated."
        
    return f"{status}: {advice}"
