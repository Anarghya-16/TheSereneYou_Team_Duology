# The Serene You

A mental wellness companion app built with Flutter, offering guided meditation, mood tracking, journaling, and an AI companion for emotional support.

## Features

- **Guided Meditation** — mindfulness, breathing, and gratitude sessions with step-by-step guidance
- **Mood Tracking** — log and review your moods over time
- **Dear Diary** — a private journal for daily entries and reflection
- **AI Companion** — a simple conversational companion that responds to how you're feeling
- Clean, calming UI built with Flutter and Material 3

## Tech Stack

**Frontend**
- [Flutter](https://flutter.dev/) / Dart
- Material 3 design

**Backend**
- [Flask](https://flask.palletsprojects.com/) (Python)
- SQLite for persistence (diary, meditation, journal, and AI companion history)

## Project Structure

```
TheSereneYou_Team_Duology/
├── lib/
│   ├── main.dart              # App entry point, home screen & navigation
│   ├── api_service.dart       # HTTP client for meditation/mood/diary/greeting endpoints
│   └── backend_service.dart   # Generic backend call helper
├── serene_you_backend/
│   ├── app.py                 # Flask API — diary, meditation, journal, AI companion routes
│   └── serene_you_backend.py  # Request handler logic (mood logging, meditation steps, emotional support responses)
└── test/
    └── widget_test.dart
```

## Getting Started

### Backend

1. Navigate to the backend folder:
   ```bash
   cd serene_you_backend
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the server:
   ```bash
   python app.py
   ```
   The API will start on `http://0.0.0.0:5000`.

### Frontend (Flutter app)

1. Install [Flutter](https://docs.flutter.dev/get-started/install) if you haven't already.
2. Install dependencies:
   ```bash
   flutter pub get
   ```
3. Update the backend IP in `lib/api_service.dart` and `lib/backend_service.dart` to match your machine's local IP (currently set to a placeholder `172.16.34.115:5000`).
4. Run the app:
   ```bash
   flutter run
   ```

> **Note:** The Flutter app connects to the Flask backend over your local network, so both need to be running and reachable from your device/emulator for full functionality.

## API Endpoints

| Method | Endpoint      | Description                     |
|--------|---------------|----------------------------------|
| GET/POST | `/diary`    | Create or fetch diary entries    |
| GET/POST | `/meditation` | Log or fetch meditation sessions |
| GET/POST | `/journal`  | Create or fetch journal entries  |
| GET/POST | `/ai`       | Chat with the AI companion       |

## Roadmap / Ideas

- Replace the placeholder AI companion logic with a real NLP/LLM-based model
- Add user authentication and per-user data
- Persist mood tracking with charts/trends over time

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

## License

Add a license of your choice (e.g. MIT) here.
