from flask import Flask, request

import recognizer

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/audio', methods=['POST'])
def audio_to_text():
    file = request.files.get('file')
    language = request.form.get('language')
    
    response = dict()
    response['language'] = language if language else 'en-US'
    response['text'] = recognizer.voice_to_text(file, response['language'])
    
    return response

@app.route('/text', methods=['POST'])
def text_to_audio():
    text = request.form.get('text')
    language = request.form.get('language')
    
    language = language if language else 'en-US'
    
    return recognizer.text_to_voice(text, language)