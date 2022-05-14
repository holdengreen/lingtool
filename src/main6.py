from argostranslate import package, translate
import os, sys, io
import subprocess
from os.path import exists
from gtts import gTTS

installed_languages = translate.load_installed_languages()
_t1 = None
_t2 = None
for lang in installed_languages:
    if lang.name == "Spanish":
        _t1 = lang
    if lang.name == "English":
        _t2 = lang

t = _t1.get_translation(_t2)

if len(sys.argv) < 2:
    print("pass a path to a text file as an argument")
    exit(0)

_bookfl = open(sys.argv[1], 'r')
book = _bookfl.read()
_bookfl.close()

outpath = "out/stream.mp3"
if exists(outpath):
    print("{} already exists".format(outpath))
    exit(0)

sfl = open(outpath, 'ab')

paragraphs = [p for p in book.splitlines() if len(p)]

numparagraphs = len(paragraphs)
i = 0
for p in paragraphs:
    #if(not p): continue

    print("paragraph {}/{}".format(str(int(i/2)), str(numparagraphs)))

    tr = t.translate(p)

    a1 = subprocess.Popen(['espeak', p, '-v mb-es1', '--stdout'], stdout=subprocess.PIPE)
    a2 = subprocess.Popen(["ffmpeg", "-i pipe:", "-vn", "-ar 44100", "-ac 2", "-b:a 192k", "-f mp3 pipe:"], stdin=a1.stdout, stdout=subprocess.PIPE) #"ffmpeg -i pipe: -vn -ar 44100 -ac 2 -b:a 192k -f mp3 pipe:"

    sfl.write(a2.stdout.read())

    #os.system('''espeak "{}" -ven -w speech/{}.wav'''.format(tr, str(i+1)))

    a1 = subprocess.Popen(['espeak', tr, '-v mb-us1', '--stdout'], stdout=subprocess.PIPE)
    a2 = subprocess.Popen(["ffmpeg", "-i pipe:", "-vn", "-ar 44100", "-ac 2", "-b:a 192k", "-f mp3 pipe:"], stdin=a1.stdout, stdout=subprocess.PIPE) #"ffmpeg -i pipe: -vn -ar 44100 -ac 2 -b:a 192k -f mp3 pipe:"

    sfl.write(a2.stdout.read())

    '''
    try:
        speech = gTTS(text=p, lang="es", slow=False)
        speech.write_to_fp(sfl)
        speech = gTTS(text=tr, lang="en", slow=False)
        speech.write_to_fp(sfl)
    except:
        pass
    '''
    
    i+=2

sfl.close()
