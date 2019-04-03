# script to figure out frequency of each type of subjunctive

from cltk.tag.pos import POSTag
from cltk.tokenize.word import WordTokenizer
from os import listdir

tagger = POSTag('latin')
wt = WordTokenizer('latin')

filelist = sorted([f for f in listdir('./ovid_metamorphoses') if f.endswith('txt')])

present, imperfect, perfect, pluperfect = 0, 0, 0, 0
pres_ex, impf_ex, perf_ex, plup_ex = [], [], [], []

def count_subj(filename):

    global present, imperfect, perfect, pluperfect
    global pres_ex, impf_ex, perf_ex, plup_ex

    infile = open(filename)
    raw = infile.read()
    infile.close()

    tokenized = wt.tokenize(raw)
    tokenized = [t for t in tokenized if not None]

    for t in tokenized:

        tagged = tagger.tag_crf(t)

        if len(tagged) > 1 or len(tagged) == 0 or tagged[0][1] == None:
            pass
        elif tagged[0][1][0] == 'V':
            if tagged[0][1][3:5] == 'PS':
                present += 1
                pres_ex.append(str(tagged[0][0]))
            elif tagged[0][1][3:5] == 'IS':
                imperfect += 1
                impf_ex.append(str(tagged[0][0]))
            elif tagged[0][1][3:5] == 'RS':
                perfect += 1
                perf_ex.append(str(tagged[0][0]))
            elif tagged[0][1][3:5] == 'LS':
                pluperfect += 1
                plup_ex.append(str(tagged[0][0]))
        else:
            pass

    return present, imperfect, perfect, pluperfect
    return pres_ex, impf_ex, perf_ex, plup_ex

for f in filelist:

    count_subj(f)

print(pres_ex, impf_ex, perf_ex, plup_ex)
print(f'# of pres. = {present}, ', f'# of impf. = {imperfect}, ',
    f'# of perf. = {perfect}, ', f'# of plup. = {pluperfect}')
