import json
from datetime import datetime

def handle_request(request_json):
    """
    Processes incoming JSON requests for the Serene You backend.
    Returns a JSON response based on the action requested.
    """
    try:
        request_data = json.loads(request_json)
        action = request_data.get("action")

        if action == "log_mood":
            mood = request_data.get("mood")
            if not mood:
                return json.dumps({"error": "Mood is required for logging."})
            timestamp = datetime.utcnow().isoformat() + "Z"
            return json.dumps({"action": "log_mood", "mood": mood, "timestamp": timestamp})

        elif action == "meditation":
            meditation_type = request_data.get("type")
            duration_minutes = request_data.get("duration_minutes")
            
            if not meditation_type or not isinstance(duration_minutes, int) or duration_minutes <= 0:
                return json.dumps({"error": "Meditation type and valid duration (minutes) are required."})

            # Define meditation steps based on type (can be expanded)
            steps = []
            if meditation_type == "mindfulness":
                steps = [
                    "Find a comfortable position, sitting or lying down.",
                    "Close your eyes gently if you feel comfortable.",
                    "Bring your attention to your breath, noticing the sensation of air entering and leaving your body.",
                    "Observe any thoughts or feelings without judgment, letting them pass like clouds.",
                    "When your mind wanders, gently guide it back to your breath.",
                    f"Continue for {duration_minutes} minutes, allowing yourself to be present in this moment."
                ]
            elif meditation_type == "breathing":
                steps = [
                    "Sit or lie comfortably.",
                    "Inhale slowly for 4 seconds.",
                    "Hold your breath for 4 seconds.",
                    "Exhale slowly for 6 seconds.",
                    "Repeat this breathing pattern for the duration.",
                    f"Continue for {duration_minutes} minutes, focusing on the rhythm."
                ]
            elif meditation_type == "gratitude":
                steps = [
                    "Sit or lie comfortably and take a few deep breaths.",
                    "Think of three things you are grateful for right now, no matter how small.",
                    "Feel the warmth of gratitude spreading through your body.",
                    "Hold these feelings for a moment, appreciating the simple joys.",
                    "When you're ready, gently open your eyes, carrying this feeling with you."
                ]
            else:
                steps = [f"Engage in a {duration_minutes}-minute {meditation_type} meditation."]

            return json.dumps({
                "action": "meditation",
                "type": meditation_type,
                "duration_minutes": duration_minutes,
                "steps": steps
            })

        elif action == "journal":
            prompt = request_data.get("prompt")
            entry_id = request_data.get("entry_id") # Optional
            if not prompt:
                return json.dumps({"error": "Journal prompt is required."})
            return json.dumps({"action": "journal", "prompt": prompt, "entry_id": entry_id})

        elif action == "emotional_support":
            user_message = request_data.get("message")
            if not user_message:
                return json.dumps({"error": "User message is required for emotional support."})

            # Simple AI companion logic (can be expanded with NLP/ML)
            support_message = "I hear you. It's okay to feel this way. Take a deep breath with me."
            if "great" in user_message.lower() or "good" in user_message.lower() or "happy" in user_message.lower():
                support_message = "That's wonderful to hear! I'm so glad you're feeling positive."
            elif "down" in user_message.lower() or "sad" in user_message.lower() or "bad" in user_message.lower():
                support_message = "It sounds like you're going through a tough time. Remember, it's okay to not be okay. I'm here to listen."
            elif "anxious" in user_message.lower() or "stressed" in user_message.lower():
                support_message = "It sounds like you're feeling anxious. Perhaps a quick breathing exercise could help?"

            return json.dumps({"action": "emotional_support", "message": support_message})

        elif action == "profile":
            user_name = request_data.get("user_name")
            preferences = request_data.get("preferences")

            # In a real app, you'd load/save this from a database
            # For this example, we'll return what was sent or placeholders
            current_user_name = "Guest User"
            current_preferences = {"dark_mode": False, "text_size": "medium"}

            if user_name:
                current_user_name = user_name
            if preferences and isinstance(preferences, dict):
                current_preferences.update(preferences)

            return json.dumps({
                "action": "profile",
                "user_name": current_user_name,
                "preferences": current_preferences
            })

        else:
            return json.dumps({"error": "Unknown action", "received_action": action})

    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format."})
    except Exception as e:
        return json.dumps({"error": f"An unexpected error occurred: {str(e)}"})

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Mood Tracking ---")
    mood_request = json.dumps({"action": "log_mood", "mood": "anxious"})
    print("Request:", mood_request)
    print("Response:", handle_request(mood_request))
    print("-" * 20)

    print("--- Meditation ---")
    meditation_request = json.dumps({"action": "meditation", "type": "breathing", "duration_minutes": 5})
    print("Request:", meditation_request)
    print("Response:", handle_request(meditation_request))
    print("-" * 20)

    print("--- Journaling ---")
    journal_request = json.dumps({"action": "journal", "prompt": "Today I felt grateful because...", "entry_id": "daily-001"})
    print("Request:", journal_request)
    print("Response:", handle_request(journal_request))
    print("-" * 20)

    print("--- Emotional Support (Feeling Down) ---")
    support_request_down = json.dumps({"action": "emotional_support", "message": "I'm feeling really down today."})
    print("Request:", support_request_down)
    print("Response:", handle_request(support_request_down))
    print("-" * 20)

    print("--- Emotional Support (Feeling Good) ---")
    support_request_good = json.dumps({"action": "emotional_support", "message": "I had a great day!"})
    print("Request:", support_request_good)
    print("Response:", handle_request(support_request_good))
    print("-" * 20)

    print("--- Profile Update ---")
    profile_request = json.dumps({"action": "profile", "user_name": "Serenity Seeker", "preferences": {"dark_mode": True, "text_size": "large"}})
    print("Request:", profile_request)
    print("Response:", handle_request(profile_request))
    print("-" * 20)

    print("--- Invalid Request ---")
    invalid_request = json.dumps({"action": "unknown_action"})
    print("Request:", invalid_request)
    print("Response:", handle_request(invalid_request))
    print("-" * 20)

    print("--- Invalid JSON ---")
    invalid_json_request = "{not valid json"
    print("Request:", invalid_json_request)
    print("Response:", handle_request(invalid_json_request))
    print("-" * 20)