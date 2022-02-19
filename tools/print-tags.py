from nltk.data import load
tagdict = load('help/tagsets/upenn_tagset.pickle')
for tag in tagdict:
    print(tag, '->', tagdict[tag][0])
