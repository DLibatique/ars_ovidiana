import re
import timeit
from cltk.tag.pos import POSTag

tagger = POSTag('latin')

with open('../ov_met_1_raw.txt') as f:
    raw = f.read()

f = open('../ov_met_1_xml.txt', 'w+')
for (x,y) in tagger.tag_ngram_123_backoff(raw):
    f.write("<token postag='" + str(y) + "' cite=''>" + str(x) + '</token>')
