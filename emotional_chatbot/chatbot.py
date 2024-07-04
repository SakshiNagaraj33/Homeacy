from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from emotion_detector import detect_emotion

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

conversation_history = []

# Predefined responses for emotions
predefined_responses = {
    "happy": "I'm glad to hear that you're happy! Keep smiling!",
    "sad": "I'm sorry to hear that you're feeling sad. I'm here for you.",
    "angry": "It's okay to feel angry sometimes. Try to take deep breaths.",
    "anxious": "I understand that you're feeling anxious. Let's take it one step at a time.",
    "confused": "It's alright to feel confused. Can I help clarify anything?",
    "excited": "That's exciting! Tell me more about it!",
    "bored": "Feeling bored? Maybe we can find something fun to talk about.",
    "tired": "You must be really tired. Make sure to get some rest.",
    "lonely": "Feeling lonely can be tough. I'm here to chat with you.",
    "love": "Love is a beautiful emotion. Tell me more about what you're feeling.",
    "neutral": "Tell me more about how you're feeling.",
    "fearful" : "Its okay calm down ."
}

def get_response(user_message):
    # Detect emotion in user message
    emotion = detect_emotion(user_message)
    
    # Use predefined response if available
    if emotion in predefined_responses:
        bot_response = predefined_responses[emotion]
    else:
        # Append the user message and detected emotion to the conversation history
        conversation_history.append(f"User ({emotion}): {user_message}")

        # Concatenate the conversation history into a single input string
        input_text = " ".join(conversation_history)

        # Encode the input text and generate a response using the model
        inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
        outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)

        # Append the model's response to the conversation history
        conversation_history.append(f"Bot: {response}")

        bot_response = response

    return bot_response
