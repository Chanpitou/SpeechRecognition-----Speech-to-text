import speech_recognition

recognizer = speech_recognition.Recognizer()
pause = False
count = 0
# Run the program indefinitely for speech input, until condition break
while True:
    count += 1
    try:
        # open microphone as source, account for ambient noice, and capture speech/voice
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            audio = recognizer.listen(source)

            # using Google Web Speech API to recognize the captured audio/speech
            text = recognizer.recognize_google(audio)
            text = text.lower()
            # condition to stop the program
            if "mirror off" in text:
                print("screen off")
                pause = True
            elif "mirror on" in text:
                print("screen on")
                pause = False
            # display the text if not paused
            if not pause:
                print(f"Recognized: {text}")
    # to catch/display error(s)
    except speech_recognition.UnknownValueError:
        if not pause:
            print("Can't understand you, speak clearer and louder")
            print(count)
    except speech_recognition.RequestError as e:
        if not pause:
            print(f"Could not request results from Google Web Speech API; {e}")
