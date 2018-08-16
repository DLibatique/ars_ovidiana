'''

<lb n="___">
<token tok-pos="___" postag="___" lemma="___" cite="____">_____</token>
...

Pipeline:
1. get raw text
2. use jv replacer
3. tokenize into lines
4. assign line numbers with enumerate()
5. for each tuple in the enumerate object, write an l element with
    line number and CTS URN attributes that wraps the whole line


'''

from cltk.tokenize.line import LineTokenizer
from cltk.tokenize.word import WordTokenizer
from cltk.tag.pos import POSTag
from cltk.stem.lemma import LemmaReplacer
from cltk.stem.latin.j_v import JVReplacer

import re

import pprint

#initialize tokenizers, postagger, replacers
line_tokenizer = LineTokenizer('latin')
word_tokenizer = WordTokenizer('latin')
#remember to pass words into POS tagger with .lower()
pos_tagger = POSTag('latin')
lemmatizer = LemmaReplacer('latin')
jv_replacer = JVReplacer()

#get file and record to variable
infile = open('../ovid_metamorphoses/ov_met_02.txt')
raw = infile.read()
infile.close()

#replace j's and v's
jv_ed = jv_replacer.replace(raw)

#tokenize into lines
line_ed = line_tokenizer.tokenize(jv_ed)

#assign line numbers
line_assigned = enumerate(line_ed, 1)

#create line beginning milestones and token objects between with appropriate attributes
ugly_xml_string_total = ''
for a,b in line_assigned:
    #get lb element with attributes
    ugly_xml_string_line = ''
    ugly_xml_string_line += '<lb n="' + str(a) + '" cite="urn:cts:latinLit:phi0959.phi006:2.' + str(a) + '"/>'

    #get token elements with attributes
    ugly_xml_string_tokens = ''
    tok_pos_list = list(enumerate(word_tokenizer.tokenize(b), 1))

    for tok in word_tokenizer.tokenize(b):

        #assign token position in line to variable
        for x,y in tok_pos_list:
            if tok == y:
                token_position = str(x)
            else:
                pass

        #assign postag to variable
        #pass token with .lower()
        tagged_tok = pos_tagger.tag_ngram_123_backoff(tok.lower())

        #empty token (?)
        if tagged_tok == []:
            postag = 'None'

        elif len(tagged_tok) > 1:
            postag = tagged_tok[1][1]

        elif not tagged_tok[0][1]:
            postag = 'None'

        else:
            postag = tagged_tok[0][1]

        #assign lemma to variable
        l_tok = lemmatizer.lemmatize(tok.lower())

        if l_tok == []:
            lemma = 'None'

        elif l_tok[0] == '"':
            lemma = "'"

        elif len(l_tok) > 1:
            lemma = l_tok[1]

        else:
            lemma = l_tok[0]

        #assign CTS URN to variable
        citation = 'urn:cts:latinLit:phi0959.phi006:2.' + str(a)

        #concatenate token elements
        ugly_xml_string_tokens += f'<token tok-pos="{token_position}" postag="{postag}" lemma="{lemma}" cite="{citation}">' + tok + '</token>'

    #concatenate full unit (lb milestone and all tokens within line) and add to overall string
    ugly_xml_string_total += ugly_xml_string_line + ugly_xml_string_tokens

outfile = open('text.xml', 'w')
outfile.write(ugly_xml_string_total)
outfile.close()
