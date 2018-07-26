from cltk.tokenize.word import WordTokenizer

word_tokenizer = WordTokenizer('latin')

infile = open('ovid_metamorphoses/ov_met_01.txt')
raw = infile.read()
infile.close()

tokenized = word_tokenizer.tokenize(raw)

outfile = open('../ov_met_1_raw.txt', 'w')
for item in tokenized:
    outfile.write(item + ' ')
outfile.close()
