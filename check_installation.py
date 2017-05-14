import os
import sys

directory, installation_directory, version = "Fiorano", sys.argv[1], 11
property_file = os.path.join(installation_directory, directory, str(version), "build.properties")


def get_build_number(self):
    content_string = []
    try:
        file = open(property_file)
        for line in file.read():
            # print(line, end="")
            content_string.append(line)
        file.close()
        print(content_string[-7:-2])
        build_number = ''.join(content_string[-7:-2])
        return directory+build_number
        pass
    except FileNotFoundError:
        print('The file build.properties did not exist in the specified path: ', property_file)
    pass
pass


def check_product_installation(self):
    try:
        os.chdir(installation_directory)
        directory_list = os.listdir(installation_directory)
        for directory_name in directory_list:
            if directory_name == "Fiorano":
                new_directory = get_build_number(installation_directory)
                os.rename('Fiorano', new_directory)
                pass
            pass
        pass
    except ValueError:
        print('Passed String is not of String type')
        pass
    except OSError:
        print('Passed installation_directory  is not valid for the Platform')
        pass
    pass
pass

check_product_installation(sys.argv[1])
