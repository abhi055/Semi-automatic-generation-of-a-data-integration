import re
class Finder():

    def __init__(self,root):
        self.root = root
        self.classes = {}
        self.anonimous_class = {}

    def find_concepts_and_attributes(self):
        for child in self.root:
            id = child.attrib['id']
            style = child.attrib["style"] if "style" in child.attrib else ""
            value = child.attrib["value"] if "value" in child.attrib else ""

            # try:
            #     if 'rounded=0' in style:


            print(value)

    def find_elements(self):
        label_class,anonimous_class = self.find_concepts_and_attributes()
        return label_class,anonimous_class