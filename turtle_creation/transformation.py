from turtle_creation.finding import *
import re

def transform_ontology(root):
    finder = Finder(root)
    label_class, anonimous_class = finder.find_elements()

