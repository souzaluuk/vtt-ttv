import speech_recognition as sr
from flask import send_file
from gtts import gTTS

recognizer = sr.Recognizer()

def voice_to_text(file, language):
    response = ''
    if not file:
        return response

    voice = sr.AudioFile(file)
    max = 60  # in ms

    with voice as source:
        recognizer.adjust_for_ambient_noise(source)
        if source.DURATION < max:
            audio = recognizer.record(source)
        else:
            audio = recognizer.record(source, duration=max)
        response = recognizer.recognize_google(audio, language=language)

    return response

def text_to_voice(text, language):
    name_file = '.tmp.mp3'
    tts = gTTS(text, lang=language)

    with open(name_file, 'wb') as file:
        tts.write_to_fp(file)

    return send_file(name_file, mimetype='audio/mp3')
