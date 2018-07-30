# idea = get text from xml and print into appropriate lines

import lxml.etree as ET

tree = ET.parse('../ov_met_01.xml')
root = tree.getroot()

# go through tokens sequentially and print tokens out
# when token changes cite attribute, put on a new line

for num in range(1,779):

    for x in root.findall('token')[0:100]:

        line_tokens = []

        if x.get('cite') == str('urn:cts:latinLit:phi0959.phi006:1.' + str(num)):

            line_tokens.extend(x)

            line_text = ''

            for item in line_tokens:

                line_text += item.text + ' '

                print(line_text)
