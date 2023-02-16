import xml.etree.ElementTree as ET
import re

xmlfile='sub class.xml'

tree = ET.parse(xmlfile)
root = tree.getroot()

# ET.dump(tree)

# for ele in root.findall(".//mxCell[@value]"):

#     a = ele.attrib['value']
   
#     if re.search('<span>',a):
#         b = re.search('>(.*)<',a)
#         print(b.group(1))
#     else:
#         print(a)



for ele in root.findall(".//mxCell[@value][@style]"):

    shape = ele.attrib['style']
    if re.search('doubleEllipse',shape) or re.search('rounded=0',shape):
        a = ele.attrib['value']
        print(a)
        # b = re.search('>(.*)<',a)
        # print(b.group(1))
    elif re.search('ellipse',shape):
        a = ele.attrib['value']
        print(a)
        
    


