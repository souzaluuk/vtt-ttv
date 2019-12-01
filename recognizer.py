import speech_recognition as sr
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
