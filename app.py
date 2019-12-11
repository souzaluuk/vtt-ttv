from flask import Flask, request, render_template

import recognizer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/audio', methods=['POST'])
def audio_to_text():
    file = request.files.get('file')
    language = request.form.get('language')

    response = dict()
    response['language'] = language if language in ['pt-BR','en-US'] else 'en-US'
    response['text'] = recognizer.voice_to_text(file, response['language'])
    
    return response['text']

@app.route('/text', methods=['GET'])
def text_to_audio():
    text, language = map(request.args.get,['text','language'])
    
    language = language if language in ['en','pt'] else 'pt'
    
    return recognizer.text_to_voice(text, language) if text else ''