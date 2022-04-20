#beauty touch
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

print('\n')
print(Fore.GREEN + '1.  Put file which needs to be transcripted')
print(Fore.GREEN + 'in the same directory with this program.')
print(Fore.GREEN + '2.  Input "y" to select file and start transcripting.\n')

agreement = '0'
while agreement != 'y':
    agreement = input()

#
#audio converter
#

from os import path
from pydub import AudioSegment

# files
from easygui import fileopenbox
                                                                         
src = fileopenbox()
dst = "temp.wav"

#quality settings
sound = AudioSegment.from_file(src, format='m4a') # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# export file as .wav                                                            
sound.export(dst, format="wav")

#
#speech recognizer
#

import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
# open audio file
wf = wave.open('temp.wav', "rb")

# Initialize model
model = Model("vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, wf.getframerate())

import json

# Container to store our results
transcription = []

while True:
    data = wf.readframes(16000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Convert json output to dict
        result_dict = json.loads(rec.Result())
        # Extract text values and append them to transcription list
        transcription.append(result_dict.get("text", ""))

# Get final bits of audio and flush the pipeline
final_result = json.loads(rec.FinalResult())
transcription.append(final_result.get("text", ""))

# merge or join all list elements to one big string
transcription_text = ' '.join(transcription)

#create filename
outputfile = path.splitext(src)[0]
while path.exists(outputfile + '.txt'):
    outputfile = outputfile + '1'

with open(outputfile + '.txt', 'w') as f:
    f.write(transcription_text)

print('\n')
print(Fore.GREEN + 'Transcription completed successfully.')
print(Fore.GREEN + 'Result file created with name "' + outputfile + '.txt".')
print(Fore.GREEN + 'You may close program now.')
print(Fore.GREEN + 'Input "y" to end.\n')

agreement2 = '0'
while agreement2 != 'y':
    agreement2 = input()