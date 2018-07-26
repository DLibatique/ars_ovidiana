import re
import timeit
from cltk.tag.pos import POSTag

#initialize POS tagger
tagger = POSTag('latin')

#get text to POS tag
with open('../ov_met_1_raw.txt') as f:
    raw = f.read()

#parse every token
#write xml as text strings (i know it's bad, sorry)
f = open('../ov_met_1_xml.txt', 'w+')
for (x,y) in tagger.tag_ngram_123_backoff(raw):
    f.write("<token postag='" + str(y) + "' cite=''>" + str(x) + '</token>')
