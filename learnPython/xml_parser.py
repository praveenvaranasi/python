from xml.etree import ElementTree as ET
import os


def parse_xml():
    try:
        print(os.getcwd())
        xml_tree = ET.parse('configs.xml')  # Reads xml file (ET = Element tree (reads entire xml -
        # - structure and stores in s tree format))
        result = xml_tree.getroot()  # Gives root element
        print(result.tag)  # prints the tag name of the root
        for child in result:  # iterating over the root's children node
            print(child.tag, child.attrib)
            pass
    except FileNotFoundError:
        print("The file you want to use is not there in the specified location")
    pass


def accessing_elements():
    """This definition shows the functionality of few methods related to xml processing"""
    try:
        xml_tree = ET.parse('Configs.xml')
        xml_tree.getroot()

        pass
    except FileNotFoundError:
        print("The file you are trying to use is not present in the specified location")
        pass
if __name__ == "__main__":
    parse_xml()
    pass
