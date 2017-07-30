import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element


def microservice_resources():
    try:
        xml_tree = ET.ElementTree()
        # xml_tree = ElementTree.parse("/root/Desktop/OldServiceDescriptor.xml")
        # root = xml_tree.getroot()
        # print(root.tag)
        # deployment_element = root.findall('deployment')
        # deployment_tag = deployment_element[0].tag
        # resources_element = deployment_element[0].findall('resources')
        # print(resources_element[0].tag)
        # elem = ElementTree.Element(resources_element[0].tag)
        # sub_elem = ElementTree.SubElement(elem, 'hello')
        # last_elem = ElementTree.dump(elem)
        # print(sub_elem)
        # ElementTree.dump(xml_tree)
        # task = ElementTree.Element(resources_element[0].tag)
        # trying = ElementTree.SubElement(task, 'hello')
        # xml_tree.ElementTree.write("/root/Desktop/Outputfinal")

        tree = ET.parse('/root/Desktop/OldServiceDescriptor.xml')
        # tree.parse("/root/Desktop/OldServiceDescriptor.xml")
        root = tree.getroot()
        deployment_elem = (root.findall('deployment'))[0]
        resources_elem = (deployment_elem.findall('resources'))[0]
        print(resources_elem)
        resources_elem.set('updated', 'yes')
        elem = ET.Element(resources_elem)
        sub_elem = ET.SubElement(elem, 'resource')
        # tree.write('/root/Desktop/Outputshow.xml')
        # root.insert([4][0], sub_elem)
        root.insert(resources_elem, sub_elem)
        tree.write('/root/Desktop/Outputshow.xml')


    except TypeError:
        # print('The attribute you are looking for is not appearing here')
        pass
if __name__ == "__main__":
    microservice_resources()
    pass
