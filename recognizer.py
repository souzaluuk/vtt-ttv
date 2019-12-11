import speech_recognition as sr
from flask import send_file
from gtts import gTTS
from pydub import AudioSegment
from hashlib import sha1

def voice_to_text(file, language):
    recognizer = sr.Recognizer()
    
    response = ''
    if not file:
        return response

    voiceFile = sr.AudioFile(file)
    max = 60  # in ms
    
    audio = None
    with voiceFile as source:
        if source.DURATION < max:
            audio = recognizer.record(source)
        else:
            audio = recognizer.record(source, duration=max)

    return recognizer.recognize_google(audio, language=language) if audio else ''

def text_to_voice(text, language):
    path_tmp = '/tmp/'
    
    gen_hash = sha1()
    gen_hash.update(bytes(text,'utf-8'))
    
    name_file_mp3 = path_tmp+gen_hash.hexdigest()+'.mp3'
    name_file_wav = path_tmp+gen_hash.hexdigest()+'.wav'
    
    tts = gTTS(text, lang=language)

    with open(name_file_mp3, 'wb') as file:
        tts.write_to_fp(file)

    sound = AudioSegment.from_mp3(name_file_mp3)
    sound.export(name_file_wav, format='wav')
    
    return send_file(name_file_wav,attachment_filename="audio.wav",as_attachment=True)
