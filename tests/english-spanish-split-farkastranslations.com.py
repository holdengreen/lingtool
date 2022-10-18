import re

fl = open("res/foreign/parallel-translations/Verne_Jules-Voyage_au_Centre_de_la_Terre-fr-en-es-hu-nl.farkastranslations.com/Verne_Jules-Voyage_au_Centre_de_la_Terre-fr-en-es-hu-nl.txt", 'r')
t = fl.read()
fl.close()

#print(ascii(t))

t = t.split('\n')[:6]

#t = ''.join(t)

for e in t:
    g = re.split(r'\t+', e)
    print(g[1])
    print()
    print(g[2])
    print()
