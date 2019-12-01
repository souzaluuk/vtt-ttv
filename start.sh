#!/bin/bahs

sudo pip install virtualenv

virtualenv ./

source ./bin/activate^C
pip install flask gTTS SpeechRecognition

echo "To start server: flask run"