from audio import MP3File, WAVFile, FLACFile

mp3 = MP3File("audio.mp3")
mp3.play()

wav = WAVFile("audio.wav")
wav.play()

flac = FLACFile("audio.flac")
flac.play()

print()
print("=============Playlist=============")

mp3v2 = MP3File("audio2.mp3")
wav2 = WAVFile("audio2.wav")  # Define wav2 here
files = [mp3, wav, flac, mp3v2, wav2]
for i in range(len(files)):
    files[i].play()
