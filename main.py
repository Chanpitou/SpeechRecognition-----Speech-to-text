import speech_recognition

recognizer = speech_recognition.Recognizer()

# Run the program indefinitely for speech input, until condition break
while True:
    # open microphone as source, account for ambient noice, and capture speech/voice
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.9)
        audio = recognizer.listen(source)

    try:
        # using Google Web Speech API to recognize the captured audio/speech
        text = recognizer.recognize_google(audio)
        text = text.lower()
        # display the text
        print(f"Recognized: {text}")
        # condition to stop the program
        if text == "mirror off":
            break
    # to catch/display error(s)
    except speech_recognition.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
