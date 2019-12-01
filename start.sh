#!/bin/bash

sudo pip install virtualenv

virtualenv ./

source ./bin/activate
pip install flask gTTS SpeechRecognition

echo "To start server: flask run"
