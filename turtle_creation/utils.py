import xml.etree.ElementTree as ET
import base64
from urllib.parse import unquote
import zlib

def read_drawio_xml(diagram_path):

    tree = ET.parse(diagram_path)
    mxfile = tree.getroot()

    try:
        diagram = mxfile[0]
        mxGraphModel = diagram[0]
        root = mxGraphModel[0]
    except:
        # This lines are for compressed XML files
        diagram = mxfile[0]
        compressed_mxGraphModel = diagram.text
        coded_xml = base64.b64decode(compressed_mxGraphModel)
        xml_string = unquote(zlib.decompress(coded_xml, -15).decode('utf8'))
        mxGraphModel = ET.fromstring(xml_string)
        root = mxGraphModel[0]

    # Eliminate children related to the whole white template
    for elem in root:
        if elem.attrib["id"][-1] == "0":
            root.remove(elem)
            break
    for elem in root:
        if elem.attrib["id"][-1] == "1":
            root.remove(elem)
            break

    return root