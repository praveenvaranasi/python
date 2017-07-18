from xml.etree import ElementTree as ET
import os
import sys


def parse_xml():
    try:
        print(os.getcwd())

        xml_tree = ET.parse('..\Configs.xml')
        root = xml_tree.getroot()
        root.tag
    except FileNotFoundError:
        print("The file you want to use is not there in the specified location")
    pass


if __name__ == "__main__":
    parse_xml()
    pass
