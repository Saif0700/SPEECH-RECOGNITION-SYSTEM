import speech_recognition as sp

# Initializing recognizer
recognizer = sp.Recognizer()

# Using microphone for input
with sp.Microphone() as source:
    print("Say Something...")
    audio = recognizer.listen(source)

# Exception Handling if Voice Not Recognized.
try:
    text = recognizer.recognize_google(audio)
    print(f"You Said: {text}")
except sp.UnknownValueError:
    print("Speech Recognition could not recognize audio.")