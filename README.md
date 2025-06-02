
# JARVIS - Interactive AI Voice Assistant 🤖

![Version](https://img.shields.io/badge/Version-1.0-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to **JARVIS**, your sleek, voice-activated AI assistant inspired by the iconic AI from Iron Man! Built with Python and Pygame, JARVIS combines a modern dark-themed UI with dynamic voice interaction, helping you with productivity, entertainment, and system control — all at your voice command! 🚀

---

## 🎥 Demo

Click the image below to watch JARVIS in action:

[![JARVIS Demo](https://github.com/user-attachments/assets/e0f3ff7b-155c-4d81-a638-c5da71330d29)](https://drive.google.com/file/d/1Vq1t1NOpXUUKhTkk02JzrpGYn6Yqf1JG/view?usp=sharing)



---

## ✨ Features

* **Voice Activation**: Trigger with "Hey Jarvis," SPACE key, or mouse click.
* **Commands**:

  * Time & Date queries
  * Weather updates (mock data)
  * Set and read reminders
  * Math calculations
  * News headlines (mocked)
  * Wikipedia searches
  * Open system apps (Notepad, Calculator, File Explorer)
  * Screenshot capture with timestamp
  * Play music from your folder
  * System info (CPU, memory)
  * Open websites (YouTube, Google)
  * Tell jokes
* **UI**: Dark-themed with animated voice visualizer and interactive controls.
* **Controls**: SPACE to listen, ESC to exit, clickable interface.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* Microphone for voice input
* Internet connection for Wikipedia and future APIs

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mmanikandan281/Jarvis-Voice-Assistant.git
   cd Jarvis-Voice-Assistant
   ```

2. **Create and activate a virtual environment:**

* On **Windows (PowerShell)**:

  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

* On **macOS/Linux**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run JARVIS:**

   ```bash
   python jarvis.py
   ```

---

### Why is the `venv` folder excluded?

The `venv` directory contains system-specific binaries and installed packages which can be large and vary across machines. To keep this repository clean and lightweight, the `venv` folder is excluded via `.gitignore`. You can recreate the environment anytime using the steps above.

---

## 🧩 Dependencies

* `pygame` — UI rendering
* `pyttsx3` — Text-to-speech
* `SpeechRecognition` — Voice command processing
* `wikipedia` — Fetch summaries
* `pyautogui` — Screenshots
* `pyjokes` — Joke generator
* `psutil` — System info
* `requests` — API calls preparation

Install all dependencies via:

```bash
pip install pygame pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes psutil requests
```

---

## 📂 Project Structure

* `jarvis.py` — Main application and AI logic
* `reminders.txt` — Stores reminders
* `screenshots/` — Captured screenshots
* `requirements.txt` — Python dependencies list

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m "Add feature xyz"`)
4. Push the branch (`git push origin feature-xyz`)
5. Open a Pull Request

Please keep code clean, well-commented, and consistent.

---

## 📜 License

MIT License — See the [LICENSE](LICENSE) file.

---

## 🙌 Acknowledgements

* Inspired by Tony Stark's JARVIS
* Built with awesome open-source libraries and the Python community

---

## 📬 Contact

Found an issue or want to contribute?

* Open an issue on [GitHub](https://github.com/mmanikandan281/Jarvis-Voice-Assistant)
* Email: \[[your-email@example.com](mailto:your-mmanikandan281@gmail.com)] 

Developed By Manikandan M
