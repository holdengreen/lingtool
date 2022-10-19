import re

import sys

import torch

import numpy as np
MAX_WAV_VALUE = 32768.0

sample_rate = 48000

accelerator = 'cpu'
device = torch.device(accelerator)

class SpanishTTS:
    language = 'es'
    model_id = 'v3_es'
    speaker = 'es_1'

    def __init__(self):
        self.model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                model='silero_tts',
                                                language=self.language,
                                                speaker=self.model_id)

        self.model.to(device)  # gpu or cpu

    def apply(self, text):
        return self.model.apply_tts(text=text,
                        speaker=self.speaker,
                        sample_rate=sample_rate) * MAX_WAV_VALUE


class EnglishTTS:
    language = 'en'
    model_id = 'v3_en'
    speaker = 'en_117'

    def __init__(self):
        self.model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                model='silero_tts',
                                                language=self.language,
                                                speaker=self.model_id)

        self.model.to(device)  # gpu or cpu

    def apply(self, text):
        return self.model.apply_tts(text=text,
                        speaker=self.speaker,
                        sample_rate=sample_rate) * MAX_WAV_VALUE


spanishtts = SpanishTTS()
englishtts = EnglishTTS()


FFMPEG_BIN = "ffmpeg"

import subprocess as sp
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read



fl = open("res/foreign/parallel-translations/Verne_Jules-Voyage_au_Centre_de_la_Terre-fr-en-es-hu-nl.farkastranslations.com/Verne_Jules-Voyage_au_Centre_de_la_Terre-fr-en-es-hu-nl.txt", 'r')
t = fl.read()
fl.close()


errfl = open("log/err.txt", 'a+')


proc = sp.Popen([ FFMPEG_BIN,
       '-y', # (optional) means overwrite the output file if it already exists.
       "-f", 's16le', # means 16bit input
       "-acodec", "pcm_s16le", # means raw 16bit input
       '-ar', str(sample_rate), # the input will have 44100 Hz
       '-ac','1', # the input will have 2 channels (stereo)
       '-i', 'pipe:0', # means that the input will arrive from the pipe
       '-vn', # means "don't expect any video input"
       '-acodec', "libopus", # output audio codec
       '-b:a', "112k", # output bitrate (=quality). Here, 3000kb/second
       'streams/center-earth-journey-es-en-1.ogg',
       '-loglevel', 'debug'
       ],
        stdin=sp.PIPE,stdout=errfl, stderr=errfl, shell=False)


#flags = fcntl(proc.stdout, F_GETFL) # get current p.stdout flags
#fcntl(proc.stdout, F_SETFL, flags | O_NONBLOCK)


def readlines():
    #print(proc.stdout.readlines())

    #while True:
    while False:
        try:
            print(read(proc.stdout.fileno(), 1024))
        except OSError:
            # the os throws an exception if there is no data
            print('[No more data]')
            break


    '''
    for ln in proc.stdout:
        if not ln:
            break
        print(ln)
    '''
    
    '''
    while True:
        line = proc.stdout.readline()
        if not line:
            break

        print(line)
    '''

readlines()

#with proc.poll():proc.stdout.readline())

#while proc.poll() is None:
#    print(proc.stdout.readline())

#print(ascii(t))

#english,spanish english,spanish
t = t.split('\n')#[:6]

#t = ''.join(t)

max_ln = len(t)
ln_cnt = 1
for e in t:
    print("processing {0}/{1}".format(str(ln_cnt), str(max_ln)))

    g = re.split(r'\t+', e)

    try:

        #spanish
        proc.stdin.write(np.asarray(spanishtts.apply(g[2]), dtype=np.int16).tobytes())

        #1 second pause
        proc.stdin.write(np.asarray([0] * sample_rate, dtype=np.int16).tobytes())


        # english
        proc.stdin.write(np.asarray(englishtts.apply(g[1]), dtype=np.int16).tobytes())

        #2 second pause
        proc.stdin.write(np.asarray([0] * (sample_rate*2), dtype=np.int16).tobytes())

    except Exception as e:
        print(repr(e))
        
        print("occured for lines: ")
        print(g[2])
        print(g[1])


    ln_cnt += 1


