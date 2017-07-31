import xml.etree.ElementTree as ET


def microservice_resources():
    """ The module adds resources"""
    try:
        tree = ET.parse('/root/Desktop/installed/ServiceDescriptor.xml')
        root = tree.getroot()
        deployment_elem = (root.findall('deployment'))[0]
        resources_elem = (deployment_elem.findall('resources'))[0]
        elem = ET.Element(resources_elem)
        sub_elem = ET.SubElement(elem, 'resource')
        sub_elem.set('name', 'postgresql-9.1-901.jdbc3.jar')
        resources_elem.insert(0, sub_elem)
        tree.write('/root/Desktop/installed/Fiorano/11/runtimedata/repository/components/jdbc/4.0/ServiceDescriptor.xml')

    except AttributeError:
        print('The attribute you are looking for is not appearing here')
    except FileNotFoundError:
        print('The file is not present in the specified location')

if __name__ == "__main__":
    microservice_resources()
    pass
