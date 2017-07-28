from xml.etree import ElementTree


def microservice_resources():
    try:
        xml_tree = ElementTree.parse("D:\Fiorano\AdditionOfJarsToEPT\OldServiceDescriptor.xml")
        root = xml_tree.getroot()

        print(root,root.tag)
        deployment_element = root.findall('deployment')
        print(deployment_element)
        resources = deployment_element[0].tag
        print(resources)
        if resources == "deployment":
            print('Finally, you did it dude')
        for final_check in deployment_element[0]:
            print(final_check.tag, final_check.attrib)

        # substitute to the above block of code
        # Nested for loops retrieve all the elements, sub-elements, sub-sub-elements of the 'deployment' tag
        # for atts in root.findall('deployment'):
        #     print(atts.tag, atts.attrib)
        #     print(atts.get('label'))
        #     for sub_atts in atts.findall('resources'):
        #         print(sub_atts.tag)
        #         for sub_sub_atts in sub_atts.findall('resource'):
        #             print(sub_sub_atts.tag)

        # process of directly accessing elements from an xml tree
        # for attributes in root.iter('resource'):
        #     print(attributes.tag, attributes.attrib)

    except AttributeError:
        print('The attribute you are looking for is not appearing here')

if __name__ == "__main__":
    microservice_resources()
    pass
