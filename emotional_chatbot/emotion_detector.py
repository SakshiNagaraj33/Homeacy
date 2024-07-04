import re

def detect_emotion(user_message):
    patterns_emotions = {
        r'\b(happy|joy|glad|excited|thrilled|eager|grateful|thankful|appreciative|love|affectionate|fond|content|serene|peaceful|calm|hopeful|optimistic|proud|accomplished|amused|entertained|curious|inquisitive|playful)\b': "positive",
        r'\b(sad|unhappy|down|depressed|melancholy|grief|sorrow|heartbroken|hurt|guilty|remorseful|ashamed|embarrassed|disappointed|regretful)\b': "sad",
        r'\b(angry|mad|furious|irritated|resentful|disgusted|repulsed|contempt|jealous|envious)\b': "angry",
        r'\b(anxious|nervous|worried|stressed|overwhelmed|frustrated)\b': "anxious",
        r'\b(confused|puzzled|bewildered)\b': "confused",
        r'\b(bored|uninterested|apathetic|indifferent)\b': "bored",
        r'\b(tired|exhausted|weary|sleepy|fatigued|grumpy|irritable|moody|agitated|aggressive|hostile|annoyed)\b': "tired",
        r'\b(lonely|isolated|abandoned)\b': "lonely",
        r'\b(distrustful|paranoid|fearful|afraid|scared|worried|nervous|apprehensive|terrified|shocked|surprised)\b': "fearful",
        r'\b(neutral|indifferent|uncertain|conflicted|ambivalent|mixed feelings|overwhelmed|contemplative)\b': "neutral"
    }

    user_message_lower = user_message.lower()

    for pattern, emotion in patterns_emotions.items():
        if re.search(pattern, user_message_lower):
            return emotion

    return "neutral"

# Example usage:
message = "I feel excited about the upcoming trip, but also a bit anxious about the travel arrangements."
emotion = detect_emotion(message)
print(f"The detected emotion is: {emotion}")