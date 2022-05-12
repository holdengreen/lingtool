#import nltk

#sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
#tokens = nltk.word_tokenize(sentence)
#print(tokens)

excerpt = """
Donde se prosiguen los innumerables trabajos que el
bravo don Quijote y su buen escudero Sancho Panza pasaron en la venta
que, por su mal, pensó que era castillo

Donde se cuentan las razones que pasó Sancho Panza
con su señor Don Quijote, con otras aventuras dignas de ser
contadas

De las discretas razones que Sancho pasaba con su
amo, y de la aventura que le sucedió con un cuerpo muerto, con otros
acontecimientos famosos

De la jamás vista ni oída aventura que con más poco
peligro fue acabada de famoso caballero en el mundo, como la que acabó
el valeroso don Quijote de la Mancha

"""

#tokens = nltk.word_tokenize(excerpt)
#print(tokens)

#tagged = nltk.pos_tag(tokens)

#print(tagged)

#import spacy
#from spacy.lang.es.examples import sentences

#nlp = spacy.load("es_core_news_sm")

#doc = nlp(sentences[0])
#print(doc.text)
#for token in doc:
#    print(token.text, token.pos_, token.dep_)

import sys

#doc = nlp(excerpt)
#print(doc)
#for token in doc:
#    print("({0}, {1}, {2}), ".format(token.text, token.pos_, token.dep_), file=sys.stdout)

# note: I need a simple translation that can do verbs and nouns,
# if it cannot determine accurately then there should not be a 
# translation. that could be achieved by a blacklist

#out = []
#for token in doc:
#    out.append(token.text)

excerpt_  = [paragraph  for paragraph in excerpt.splitlines()]

from argostranslate import package, translate
import os
#from gtts import gTTS

installed_languages = translate.load_installed_languages()
_t1 = None
_t2 = None
for lang in installed_languages:
    if lang.name == "Spanish":
        _t1 = lang
    if lang.name == "English":
        _t2 = lang

t = _t1.get_translation(_t2)
#print(t.translate("Hola Mundo"))

i = 0
for p in excerpt_:
    if(not p): continue
    print(p)
    tr = t.translate(p)
    print(tr)
    print()
    
    '''
    os.system('''espeak "{}" -ves -w speech/{}.wav'''.format(p, str(i)))
    os.system('''espeak "{}" -ven -w speech/{}.wav'''.format(tr, str(i+1)))
    '''

    ''''''
    speech = gTTS(text=p, lang="es", slow=False)
    speech.save("speech/"+str(i)+".mp3")
    speech = gTTS(text=tr, lang="en", slow=False)
    speech.save("speech/"+str(i+1)+".mp3")
    ''''''
    
    i+=2

