# JARVIS - Interactive AI Voice Assistant 🤖

![JARVIS Interface](https://img.shields.io/badge/Version-1.0-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to **JARVIS**, your sleek, voice-activated AI assistant inspired by the iconic AI from Iron Man! Built with Python, Pygame, and a suite of powerful libraries, JARVIS combines a modern dark-themed UI with dynamic voice interactions, making it your go-to assistant for productivity, entertainment, and system control. Get ready to command your digital world with style! 🚀

## Demo

Watch JARVIS in action: [JARVIS Demo Video](https://drive.google.com/file/d/1Vq1t1NOpXUUKhTkk02JzrpGYn6Yqf1JG/view?usp=sharing)


## ✨ Features That Shine

- **Voice-Powered Interaction**: Activate JARVIS with "Hey Jarvis," a SPACE key press, or a click anywhere on the screen.
- **Dynamic Commands**:
  - **Time & Date**: Ask "What's the time?" or "What's the date?" for instant updates.
  - **Weather Updates**: Get mock weather data (e.g., "Weather in Palakkad: 28°C, Partly Cloudy").
  - **Reminders**: Set with "Set reminder to call John" or check with "Read my reminders."
  - **Math Wizard**: Calculate with "Calculate 5 plus 10" or complex expressions.
  - **News Flash**: Hear top headlines with "Tell me news" (mocked for now).
  - **Wikipedia Search**: Query with "Wikipedia Python" for quick summaries.
  - **System Control**: Open apps like "Open Notepad," "Open Calculator," or "Open File Explorer."
  - **Screenshot Magic**: Capture with "Take screenshot" and save with timestamps.
  - **Music Vibes**: Play random tracks from your Music folder with "Play music."
  - **System Insights**: Check CPU/memory usage with "System info."
  - **Web Navigation**: Launch "Open YouTube" or "Open Google" in your browser.
  - **Joke Generator**: Lighten the mood with "Tell me a joke."
- **Stunning UI**: A dark-themed interface with animated voice visualizer, pulsing rings, and wave bars for a futuristic feel.
- **Interactive Controls**: Click, hover, or use keyboard shortcuts (SPACE to listen, ESC to exit).
- **Responsive Feedback**: Real-time status updates (Ready, Listening, Processing) with vibrant animations.

## 🚀 Get Started

### Prerequisites
- Python 3.8 or higher
- A microphone for voice input
- Internet connection (for Wikipedia and potential future API integrations)

### Installation
1. **Clone the Repo**:
   ```bash
   git clone https://github.com/mmanikandan281/Jarvis-Voice-Assistant.git
   cd Jarvis-Voice-Assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch JARVIS**:
   ```bash
   python jarvis.py
   ```

### Dependencies
Power up JARVIS with these Python libraries:
- `pygame`: Renders the sleek graphical interface.
- `pyttsx3`: Converts text to speech for JARVIS's voice.
- `speech_recognition`: Listens and processes your voice commands.
- `wikipedia`: Fetches quick info from Wikipedia.
- `pyautogui`: Captures screenshots effortlessly.
- `pyjokes`: Delivers a chuckle with random jokes.
- `psutil`: Monitors system performance.
- `requests`: Prepares for future API integrations.

Install them all with:
```bash
pip install pygame pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes psutil requests
```

## 🎮 How to Use
1. **Start JARVIS**: Run `python jarvis.py` to launch the interface.
2. **Activate Listening**:
   - Press **SPACE**.
   - Click the **Listen** button.
   - Click anywhere on the screen.
3. **Speak Commands**: Try phrases like:
   - "What's the time?"
   - "Set reminder to finish README"
   - "Open YouTube"
   - "Calculate 2 times 3 plus 5"
   - "Tell me a joke"
4. **Exit**: Say "Goodbye" or press **ESC**.
5. **Explore the UI**:
   - **Left Panel**: Lists all available commands.
   - **Center**: Shows a dynamic voice visualizer with pulsing animations.
   - **Right Panel**: Displays your last command and JARVIS's response.
   - **Footer**: Quick guide to controls.

## 📂 Project Structure
- `jarvis.py`: The heart of JARVIS, containing UI and AI logic.
- `reminders.txt`: Stores your reminders (auto-generated).
- `screenshots`: Saves your screenshots with timestamps (auto-generated).
- `requirements.txt`: Lists all required libraries.

## 🤝 Contribute to JARVIS
Want to make JARVIS even smarter? Here's how:
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature-cool-new-idea`).
3. Commit your changes (`git commit -m "Added cool new feature"`).
4. Push to your branch (`git push origin feature-cool-new-idea`).
5. Open a Pull Request with a clear description.

Please keep code clean, commented, and aligned with the existing style.

## 📜 License
JARVIS is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share!

## 🙌 Acknowledgements
- Inspired by Tony Stark's JARVIS from the Marvel Universe.
- Powered by awesome open-source libraries like Pygame, pyttsx3, and more.
- Big thanks to the Python community for making this possible.

## 📬 Get in Touch
Found a bug or have a brilliant idea? 
- Open an issue on [GitHub](https://github.com/mmanikandan281/Jarvis-Voice-Assistant).
- Reach out to the maintainer at [your-email@example.com].

---
**Command the future with JARVIS!** 🎙️ Let’s make your day smarter and more fun! 🌟
