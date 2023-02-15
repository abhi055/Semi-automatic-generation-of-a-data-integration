import xml.etree.ElementTree as ET
import re

xmlfile='Untitle.xml'

tree = ET.parse(xmlfile)
root = tree.getroot()

# ET.dump(tree)

for ele in root.findall(".//mxCell[@value]"):
    a = ele.attrib['value']
   
    if re.search('<span>',a):
        b = re.search('>(.*)<',a)
        print(b.group(1))
    else:
        print(a)




