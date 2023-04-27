# https://github.com/ggerganov/whisper.cpp
ffmpeg -i [fielname] -acodec pcm_s16le -ac 1 -ar 16000 out.wav
./main -m models/ggml-large.bin -l zh -threads 6 -olrc -ovtt -f [filename]
