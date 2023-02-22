import xml.etree.ElementTree as ET
import re
from turtle_creation.transformation import transform_ontology
from turtle_creation.utils import read_drawio_xml

def main():
    xmlfile='sub class.xml'
    root = read_drawio_xml(xmlfile)
    turtle_file_string = transform_ontology(root)
    
    return print("Hello World!")


if __name__ == "__main__":
    main()

# ET.dump(tree)

# for ele in root.findall(".//mxCell[@value]"):

#     a = ele.attrib['value']
   
#     if re.search('<span>',a):
#         b = re.search('>(.*)<',a)
#         print(b.group(1))
#     else:
#         print(a)
# xmlfile_string = transform_ontology(root)


# for ele in root.findall(".//mxCell[@value][@style]"):

#     shape = ele.attrib['style']
#     val = ele.attrib['value']
#     print(val)


#     # switcher = {
#     #     re.search('edgeLabel',shape):
#     #         if ele.attrib['value']==='U':

        
#     # }


#     if re.search('doubleEllipse',shape) or re.search('rounded=0',shape):
#         a = ele.attrib['value']
#         print(a)
#         # b = re.search('>(.*)<',a)
#         # print(b.group(1))
#     elif re.search('ellipse',shape):
#         a = ele.attrib['value']
#         print(a)
        
    


