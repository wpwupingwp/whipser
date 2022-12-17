#!/usr/bin/python3

from pathlib import Path
import whisper
import pickle

models = ('tiny', 'base', 'small', 'medium', 'large')
for i in models:
    whisper.load_model(i)
model = whisper.load_model('large')
audio = Path('1min.wav')
result = model.transcribe(str(audio), fp16=False)
with open('result', 'wb') as out:
    pickle.dump(result, out)
print(result)