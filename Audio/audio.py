class AudioFile: #abstract class, baseclass, parenet class, superclass
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recognized format")
        self.filename = filename
        
    def play(self):
        raise NotImplementedError("Superclass must be implement")
    
class MP3File(AudioFile):
    ext = "mp3"  # extension นามสกุล
    def play(self):
        print(f"Playing {self.filename} as mp3")
        
class WAVFile(AudioFile):
    ext = "wav"
    def play(self):
        print(f"Playing {self.filename} as wav")
        
#ducking-type
class FLACFile:
    ext = "flac"
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recognized format")
        self.filename = filename
    
    
    def play(self):
        print(f"Playing {self.filename} as flac")