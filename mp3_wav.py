from os import path
from pydub import AudioSegment

# files                                                                         
src = "GMT20220309.mp3"
dst = "test.wav"

#quality settings
sound = AudioSegment.from_mp3(src) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# convert mp3 to wav                                                            
sound.export(dst, format="wav")