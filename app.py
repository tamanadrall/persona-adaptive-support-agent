import json
from persona_model import detect_persona

# Load Knowledge Base
with open("kb.json", "r") as f:
    kb = json.load(f)

# Simple intent detection
def detect_intent(user_input):
    if "login" in user_input.lower():
        return "login_issue"
    elif "crash" in user_input.lower():
        return "app_crash"
    else:
        return None

# Tone adaptation
def adapt_tone(persona, intent):
    if intent not in kb:
        return "I'm escalating this issue to a human agent."

    if persona == "technical":
        return kb[intent]["technical_details"]

    elif persona == "frustrated":
        return "I'm really sorry for the inconvenience. " + kb[intent]["solution"]

    elif persona == "executive":
        return kb[intent]["business_impact"]

# Escalation logic
def should_escalate(user_input):
    negative_words = ["refund", "cancel", "legal", "complaint"]
    for word in negative_words:
        if word in user_input.lower():
            return True
    return False

# Chat loop
if __name__ == "__main__":
    print("Persona-Adaptive Support Agent Running...")
    
    while True:
        user_input = input("\nUser: ")
        
        if user_input.lower() == "exit":
            break
        
        persona = detect_persona(user_input)
        intent = detect_intent(user_input)
        
        if should_escalate(user_input):
            print("Escalating to human agent with context...")
            print(f"Persona: {persona}")
            print(f"Intent: {intent}")
            continue
        
        response = adapt_tone(persona, intent)
        print("Bot:", response)
        