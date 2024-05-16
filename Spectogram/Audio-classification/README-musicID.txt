To get the audio files for demonstrating my program working.

1) downloaded from music from https://freepd.com/

2) used sox to 
   a) trim 0 5    keep only first 5 seconds
   b) channels 1  convert to mono
   c) rate 22050  convert to fs = 22050

    sox inputFile.mp3 outputFile.wav trim 0 5 channels 1 rate 22050


