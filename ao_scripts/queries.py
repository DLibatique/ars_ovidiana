import lxml.etree as ET

#get xml tree
tree = ET.parse("../ov_met_01.xml")

#declare xml root
root = tree.getroot()

#assign variable for list of said elements
said_tags = root.xpath("//said")

def get_whole_speech():
    #get speaker, text, and citation of each direct speech
    for tag in said_tags:

        #initialize empty string
        whole_speech = ""

        #get all token elements contained in said tags
        for i in tag.findall('token'):

            #concatenate strings into a continuous speech
            whole_speech += i.text + " "

            #assign speaker, speech, and citation to variable
            speech = str(tag.get('speaker') + ":  " + whole_speech + " (" + tag.get('cite') + ")")

            #declare dict and get rid of extraneous white space near punctuation and enclitic que and ve
            replacements = {
                '" ': '"',
                ' "': '"',
                "' ": "'",
                " '": "'",
                " que ": "que ",
                " ve ": "ve ",
                " ,": ",",
                " .": ".",
                " :": ":",
                " !": "!",
                " ;": ";",
                " ?": "?"
                }

            for k,v in replacements.items():
                speech = speech.replace(k, v)

        #print speaker, full speech, and citation
        print(speech + '\n')

#find all tokens tagged with 'speech' or 'vision'
def get_speech_or_vision_words(type):

    #get all token elements in document
    tokens = root.findall('token')

    #iterate through list of token elements
    for i in tokens:

        #look for match to 'speech' or 'vision' in type attribute
        if i.get('type') == type:

            #print the word of speech or vision and the citation
            print(i.text + " (" + i.get('cite') + ")")

# get_whole_speech()
# get_speech_or_vision_words('speech')
get_speech_or_vision_words('vision')
