import pygame
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes
import requests
import json
import threading
import sys
import math
from pathlib import Path

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS - AI Voice Assistant")

# Modern Dark Theme Colors
DARK_BG = (15, 23, 42)          # Dark slate
CARD_BG = (30, 41, 59)          # Slate 700
ACCENT = (59, 130, 246)         # Blue 500
ACCENT_HOVER = (37, 99, 235)    # Blue 600
SUCCESS = (34, 197, 94)         # Green 500
WARNING = (251, 191, 36)        # Amber 400
ERROR = (239, 68, 68)           # Red 500
TEXT_PRIMARY = (248, 250, 252)  # Slate 50
TEXT_SECONDARY = (148, 163, 184) # Slate 400
BORDER = (51, 65, 85)           # Slate 600
HOVER_BG = (45, 55, 72)         # Slate 600 lighter

# Fonts
font_title = pygame.font.Font(None, 42)
font_large = pygame.font.Font(None, 32)
font_medium = pygame.font.Font(None, 24)
font_small = pygame.font.Font(None, 18)
font_tiny = pygame.font.Font(None, 16)

class ModernButton:
    def __init__(self, x, y, width, height, text, color=ACCENT):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = ACCENT_HOVER if color == ACCENT else color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        
        text_surface = font_medium.render(self.text, True, TEXT_PRIMARY)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class VoiceVisualizer:
    def __init__(self):
        self.circles = []
        self.listening = False
        self.pulse_radius = 0
        self.pulse_alpha = 255
        self.pulse_time = 0
        self.wave_offset = 0
        
    def update(self, listening):
        self.listening = listening
        if listening:
            self.pulse_time += 0.1
            self.wave_offset += 0.2
            
            # Professional pulsing effect
            self.pulse_radius += 1
            if self.pulse_radius > 60:
                self.pulse_radius = 30
                
            # Simple professional circles
            if len(self.circles) < 3:
                self.circles.append({
                    'radius': 20,
                    'alpha': 150,
                    'growth': 0.5
                })
            
            # Update circles
            for circle in self.circles[:]:
                circle['radius'] += circle['growth']
                circle['alpha'] -= 2
                if circle['alpha'] <= 0:
                    self.circles.remove(circle)
        else:
            self.circles.clear()
            self.pulse_radius = 0
    
    def draw(self, surface):
        center_x, center_y = WIDTH // 2, HEIGHT // 2 - 50
        
        if self.listening:
            # Animated pulse rings
            for i in range(3):
                alpha = int(100 - i * 30 + 30 * math.sin(self.pulse_time + i))
                radius = 80 + i * 20 + 10 * math.sin(self.pulse_time + i)
                
                pulse_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(pulse_surf, (*ACCENT[:3], max(0, alpha)), 
                                 (radius, radius), radius, 2)
                surface.blit(pulse_surf, (center_x - radius, center_y - radius))
            
            # Professional concentric circles
            for i, circle in enumerate(self.circles):
                circle_surface = pygame.Surface((circle['radius']*4, circle['radius']*4), pygame.SRCALPHA)
                alpha = max(0, circle['alpha'])
                pygame.draw.circle(circle_surface, (*ACCENT[:3], alpha), 
                                 (circle['radius']*2, circle['radius']*2), circle['radius'], 2)
                surface.blit(circle_surface, (center_x - circle['radius']*2, center_y - circle['radius']*2))
            
            # Animated wave bars
            for i in range(-5, 6):
                bar_height = 20 + 15 * math.sin(self.wave_offset + i * 0.5)
                bar_x = center_x + i * 12
                bar_rect = pygame.Rect(bar_x - 3, center_y - bar_height // 2, 6, bar_height)
                pygame.draw.rect(surface, ACCENT, bar_rect, border_radius=3)
        
        # Main microphone button
        mic_radius = 50
        mic_color = ACCENT if self.listening else BORDER
        pygame.draw.circle(surface, CARD_BG, (center_x, center_y), mic_radius + 5)
        pygame.draw.circle(surface, mic_color, (center_x, center_y), mic_radius, 3)
        
        # Microphone icon (simplified)
        mic_rect = pygame.Rect(center_x - 15, center_y - 20, 30, 25)
        pygame.draw.rect(surface, TEXT_PRIMARY, mic_rect, border_radius=15)
        pygame.draw.rect(surface, DARK_BG, mic_rect.inflate(-6, -6), border_radius=12)
        
        # Mic stand
        pygame.draw.rect(surface, TEXT_PRIMARY, (center_x - 1, center_y + 10, 2, 15))
        pygame.draw.rect(surface, TEXT_PRIMARY, (center_x - 8, center_y + 22, 16, 3))

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        
        self.status = "Ready"
        self.last_command = ""
        self.listening = False
        self.response_text = "Welcome! I'm your AI assistant. Press SPACE or say 'Hey Jarvis' to start."
        
        # Play startup sound effect
        self.speak("Voice assistant initialized. Hello, I'm Jarvis. How may I assist you today?")

    def speak(self, audio):
        def speak_thread():
            self.engine.say(audio)
            self.engine.runAndWait()
        
        thread = threading.Thread(target=speak_thread)
        thread.daemon = True
        thread.start()

    def get_weather(self, city="Palakkad"):
        try:
            self.speak(f"The weather in {city} is partly cloudy with a temperature of 28 degrees celsius")
            self.response_text = f"🌤️ Weather in {city}: 28°C, Partly Cloudy"
            return f"Weather in {city}: 28°C, Partly Cloudy"
        except:
            self.speak("Sorry, I couldn't fetch weather information")
            self.response_text = "❌ Weather service unavailable"
            return "Weather service unavailable"

    def set_reminder(self, reminder_text):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("reminders.txt", "a") as f:
            f.write(f"{timestamp}: {reminder_text}\n")
        self.speak(f"Reminder set: {reminder_text}")
        self.response_text = f"✅ Reminder saved: {reminder_text}"

    def read_reminders(self):
        try:
            with open("reminders.txt", "r") as f:
                reminders = f.readlines()
            if reminders:
                self.speak("Here are your recent reminders:")
                reminder_list = []
                for reminder in reminders[-3:]:
                    reminder_list.append(reminder.strip())
                    self.speak(reminder.strip())
                self.response_text = "📋 Recent reminders:\n" + "\n".join(reminder_list)
            else:
                self.speak("You have no reminders")
                self.response_text = "📋 No reminders found"
        except FileNotFoundError:
            self.speak("You have no reminders")
            self.response_text = "📋 No reminders found"

    def calculate(self, expression):
        try:
            expression = expression.replace("plus", "+").replace("add", "+")
            expression = expression.replace("minus", "-").replace("subtract", "-")
            expression = expression.replace("times", "*").replace("multiply", "*")
            expression = expression.replace("divided by", "/").replace("divide", "/")
            
            result = eval(expression)
            self.speak(f"The result is {result}")
            self.response_text = f"🔢 Calculation: {expression} = {result}"
            return str(result)
        except:
            self.speak("Sorry, I couldn't calculate that")
            self.response_text = "❌ Calculation error - please try again"
            return "Calculation error"

    def get_news_headlines(self):
        headlines = [
            "Technology stocks rise in morning trading",
            "Weather alert issued for coastal regions", 
            "New space mission launched successfully",
            "Local sports team wins championship",
            "New environmental protection law passed"
        ]
        self.speak("Here are today's top headlines:")
        self.response_text = "📰 Today's Headlines:\n"
        for i, headline in enumerate(headlines[:3], 1):
            self.speak(headline)
            self.response_text += f"{i}. {headline}\n"

    def open_application(self, app_name):
        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe", 
            "paint": "mspaint.exe",
            "file explorer": "explorer.exe",
            "browser": "chrome.exe",
            "task manager": "taskmgr.exe"
        }
        
        if app_name in apps:
            try:
                os.system(apps[app_name])
                self.speak(f"Opening {app_name}")
                self.response_text = f"✅ Opened {app_name.title()}"
            except:
                self.speak(f"Couldn't open {app_name}")
                self.response_text = f"❌ Failed to open {app_name}"
        else:
            self.speak("Application not found")
            self.response_text = f"❌ Application '{app_name}' not found"

    def takecommand(self):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=8)
            
            query = r.recognize_google(audio, language="en-in")
            return query.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception:
            return None

    def take_screenshot(self):
        img = pyautogui.screenshot()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        img.save(filename)
        self.speak(f"Screenshot saved as {filename}")
        self.response_text = f"📸 Screenshot saved: {filename}"

    def search_wikipedia(self, query):
        try:
            self.speak("Searching Wikipedia...")
            self.response_text = "🔍 Searching Wikipedia..."
            result = wikipedia.summary(query, sentences=2)
            self.speak(result)
            self.response_text = f"📖 Wikipedia: {result[:200]}..."
        except:
            self.speak("Couldn't find information on Wikipedia")
            self.response_text = "❌ Wikipedia search failed"

    def play_music(self):
        music_dir = os.path.expanduser("~/Music")
        if os.path.exists(music_dir):
            songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav', '.flac'))]
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                self.speak(f"Playing {song}")
                self.response_text = f"🎵 Playing: {song}"
            else:
                self.speak("No music files found")
                self.response_text = "🎵 No music files found"
        else:
            self.speak("Music directory not found")
            self.response_text = "🎵 Music directory not accessible"

    def get_system_info(self):
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            self.speak(f"CPU usage is {cpu_percent} percent. Memory usage is {memory.percent} percent")
            self.response_text = f"💻 System Info:\nCPU: {cpu_percent}%\nMemory: {memory.percent}%"
        except:
            self.speak("System information unavailable")
            self.response_text = "💻 System info unavailable"

    def process_command(self, query):
        if not query:
            return
            
        self.last_command = query.title()
        
        # Time & Date Commands
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            self.response_text = f"🕐 Current time: {current_time}"
            
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")
            self.response_text = f"📅 Today's date: {current_date}"
            
        # Weather & Environment
        elif "weather" in query:
            self.get_weather()
            
        # Productivity Commands
        elif "reminder" in query:
            if "set" in query:
                reminder = query.replace("set reminder", "").strip()
                self.set_reminder(reminder)
            else:
                self.read_reminders()
                
        elif "calculate" in query or "math" in query:
            expression = query.replace("calculate", "").replace("math", "").strip()
            self.calculate(expression)
            
        # Information Commands
        elif "news" in query:
            self.get_news_headlines()
            
        elif "wikipedia" in query:
            search_query = query.replace("wikipedia", "").strip()
            self.search_wikipedia(search_query)
            
        # System Commands
        elif "open" in query:
            app_name = query.replace("open", "").strip()
            self.open_application(app_name)
            
        elif "screenshot" in query:
            self.take_screenshot()
            
        elif "system info" in query:
            self.get_system_info()
            
        # Entertainment Commands
        elif "joke" in query:
            joke = pyjokes.get_joke()
            self.speak(joke)
            self.response_text = f"😄 {joke}"
            
        elif "music" in query:
            self.play_music()
            
        # Web Commands
        elif "youtube" in query:
            wb.open("youtube.com")
            self.speak("Opening YouTube")
            self.response_text = "🎥 Opening YouTube"
            
        elif "google" in query:
            wb.open("google.com")
            self.speak("Opening Google")
            self.response_text = "🔍 Opening Google"
            
        # Exit Commands
        elif "exit" in query or "quit" in query or "goodbye" in query:
            self.speak("Goodbye! Have a great day!")
            self.response_text = "👋 Goodbye! Have a great day!"
            return "exit"
        
        else:
            self.speak("I didn't understand that command. Please try again.")
            self.response_text = "❓ Command not recognized. Please try again."

def draw_card(surface, x, y, width, height, title="", border_radius=12):
    """Draw a modern card with rounded corners"""
    card_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, CARD_BG, card_rect, border_radius=border_radius)
    pygame.draw.rect(surface, BORDER, card_rect, 1, border_radius=border_radius)
    
    if title:
        title_surface = font_large.render(title, True, TEXT_PRIMARY)
        surface.blit(title_surface, (x + 20, y + 15))
    
    return card_rect

def draw_command_item(surface, x, y, text, icon="•"):
    """Draw a command list item"""
    icon_surface = font_medium.render(icon, True, ACCENT)
    text_surface = font_small.render(text, True, TEXT_SECONDARY)
    
    surface.blit(icon_surface, (x, y))
    surface.blit(text_surface, (x + 20, y + 2))

def draw_modern_interface(assistant, visualizer, listen_button):
    # Background
    screen.fill(DARK_BG)
    
    # Header
    header_rect = pygame.Rect(0, 0, WIDTH, 80)
    pygame.draw.rect(screen, CARD_BG, header_rect)
    pygame.draw.rect(screen, BORDER, (0, 79, WIDTH, 1))
    
    # Title and subtitle
    title = font_title.render("JARVIS - AI Voice Assistant", True, TEXT_PRIMARY)
    subtitle = font_medium.render("Professional AI Assistant System", True, TEXT_SECONDARY)
    screen.blit(title, (30, 15))
    screen.blit(subtitle, (30, 45))
    
    # Status indicator
    status_colors = {"Ready": SUCCESS, "Listening": WARNING, "Processing": ACCENT}
    status_color = status_colors.get(assistant.status, TEXT_SECONDARY)
    
    status_x = WIDTH - 200
    pygame.draw.circle(screen, status_color, (status_x, 40), 6)
    status_text = font_medium.render(assistant.status, True, status_color)
    screen.blit(status_text, (status_x + 15, 30))
    
    # Main content area
    content_y = 100
    
    # Left panel - Commands
    commands_card = draw_card(screen, 30, content_y, 420, HEIGHT - content_y - 30, "Available Commands")
    
    commands = [
        ("Time & Information", [
            "What time is it?",
            "What's the date?", 
            "What's the weather?",
            "Tell me news",
            "Wikipedia [topic]"
        ]),
        ("Productivity", [
            "Set reminder [message]",
            "Read my reminders",
            "Calculate [expression]",
            "Take screenshot",
            "System information"
        ]),
        ("System Operations", [
            "Open calculator",
            "Open notepad",
            "Open paint",
            "Open file explorer",
            "Open task manager"
        ]),
        ("Web & Media", [
            "Open YouTube",
            "Open Google",
            "Play music"
        ]),
        ("Entertainment", [
            "Tell me a joke"
        ]),
        ("Control", [
            "Exit system",
            "Goodbye"
        ])
    ]
    
    y_pos = content_y + 60
    for category, items in commands:
        # Category header
        cat_surface = font_medium.render(category, True, ACCENT)
        screen.blit(cat_surface, (50, y_pos))
        y_pos += 30
        
        # Command items
        for item in items:
            draw_command_item(screen, 70, y_pos, item)
            y_pos += 22
        y_pos += 15
    
    # Center - Voice visualizer
    visualizer.draw(screen)
    
    # Listen button
    listen_button.draw(screen)
    
    # Instructions
    instruction_text = "Press SPACE to Listen" if not assistant.listening else "Listening... Speak now!"
    instruction_color = TEXT_SECONDARY if not assistant.listening else WARNING
    instruction_surface = font_medium.render(instruction_text, True, instruction_color)
    instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    screen.blit(instruction_surface, instruction_rect)
    
    # Right panel - Response
    response_card = draw_card(screen, WIDTH - 450, content_y, 420, 450, "System Response")
    
    # Last command
    if assistant.last_command:
        cmd_label = font_small.render("Last Command:", True, TEXT_SECONDARY)
        screen.blit(cmd_label, (WIDTH - 430, content_y + 60))
        
        cmd_text = font_medium.render(assistant.last_command[:40] + "..." if len(assistant.last_command) > 40 else assistant.last_command, True, TEXT_PRIMARY)
        screen.blit(cmd_text, (WIDTH - 430, content_y + 85))
    
    # Response text
    response_y = content_y + 130
    response_lines = assistant.response_text.split('\n')
    
    for i, line in enumerate(response_lines[:15]):
        if len(line) > 45:
            line = line[:42] + "..."
        line_surface = font_small.render(line, True, TEXT_SECONDARY)
        screen.blit(line_surface, (WIDTH - 430, response_y + i * 20))
    
    # Footer
    footer_rect = pygame.Rect(0, HEIGHT - 60, WIDTH, 60)
    pygame.draw.rect(screen, CARD_BG, footer_rect)
    pygame.draw.rect(screen, BORDER, (0, HEIGHT - 60, WIDTH, 1))
    
    footer_text = font_small.render("SPACE: Activate Voice | CLICK: Quick Activate | ESC: Exit Application", True, TEXT_SECONDARY)
    footer_rect_center = footer_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    screen.blit(footer_text, footer_rect_center)
    
    pygame.display.flip()

def main():
    assistant = VoiceAssistant()
    visualizer = VoiceVisualizer()
    listen_button = ModernButton(WIDTH // 2 - 75, HEIGHT // 2 + 100, 150, 40, "🎤 Listen", ACCENT)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                elif event.key == pygame.K_SPACE:
                    if not assistant.listening:
                        assistant.status = "Listening"
                        assistant.listening = True
                        assistant.response_text = "🎤 Listening... Speak now!"
                        
                        def listen_thread():
                            query = assistant.takecommand()
                            if query:
                                assistant.status = "Processing"
                                result = assistant.process_command(query)
                                if result == "exit":
                                    pygame.quit()
                                    sys.exit()
                            else:
                                assistant.response_text = "❌ No speech detected. Try again."
                            assistant.status = "Ready"
                            assistant.listening = False
                        
                        thread = threading.Thread(target=listen_thread)
                        thread.daemon = True
                        thread.start()
            
            # Handle button clicks and mouse interactions
            if listen_button.handle_event(event):
                if not assistant.listening:
                    assistant.status = "Listening"
                    assistant.listening = True
                    assistant.response_text = "🎤 Listening... Speak now!"
                    
                    def listen_thread():
                        query = assistant.takecommand()
                        if query:
                            assistant.status = "Processing"
                            result = assistant.process_command(query)
                            if result == "exit":
                                pygame.quit()
                                sys.exit()
                        else:
                            assistant.response_text = "❌ No speech detected. Try again."
                        assistant.status = "Ready"
                        assistant.listening = False
                    
                    thread = threading.Thread(target=listen_thread)
                    thread.daemon = True
                    thread.start()
            
            # Click anywhere to activate listening
            elif event.type == pygame.MOUSEBUTTONDOWN and not listen_button.rect.collidepoint(event.pos):
                if not assistant.listening:
                    assistant.status = "Listening"
                    assistant.listening = True
                    assistant.response_text = "🎤 Listening... Speak now!"
                    
                    def listen_thread():
                        query = assistant.takecommand()
                        if query:
                            assistant.status = "Processing"
                            result = assistant.process_command(query)
                            if result == "exit":
                                pygame.quit()
                                sys.exit()
                        else:
                            assistant.response_text = "❌ No speech detected. Try again."
                        assistant.status = "Ready"
                        assistant.listening = False
                    
                    thread = threading.Thread(target=listen_thread)
                    thread.daemon = True  
                    thread.start()
        
        visualizer.update(assistant.listening)
        draw_modern_interface(assistant, visualizer, listen_button)
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()