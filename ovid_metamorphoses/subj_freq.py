from cltk.tag.pos import POSTag
from cltk.tokenize.word import WordTokenizer
from os import listdir

tagger = POSTag('latin')
wt = WordTokenizer('latin')

filelist = sorted([f for f in listdir('.') if f.endswith('txt')])

present, imperfect, perfect, pluperfect = 0, 0, 0, 0

for f in filelist:

    infile = open(f)
    raw = infile.read()
    infile.close()

    tokenized = wt.tokenize(raw)
    tokenized = [t for t in tokenized if not None]

    for t in tokenized:

        tagged = tagger.tag_ngram_123_backoff(t)

        if len(tagged) > 1 or len(tagged) == 0 or tagged[0][1] == None:
            pass
        elif tagged[0][1][0] == 'V':
            if tagged[0][1][3:5] == 'PS':
                present += 1
            elif tagged[0][1][3:5] == 'IS':
                imperfect += 1
            elif tagged[0][1][3:5] == 'RS':
                perfect += 1
            elif tagged[0][1][3:5] == 'LS':
                pluperfect += 1
        else:
            pass

print(present, imperfect, perfect, pluperfect)