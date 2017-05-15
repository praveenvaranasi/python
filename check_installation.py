import os
import sys

directory, installation_directory, version = "Fiorano", sys.argv[1], 11
property_file = os.path.join(installation_directory, directory, str(version), "build.properties")


def get_build_number(self):
    """ Gets the build number
    
        This function searches the build number in the Installation home of Fiorano and returns the build number"""

    content_string = []
    try:
        file = open(property_file)
        for line in file.read():
            # print(line, end="")
            content_string.append(line)
        file.close()
        # print(content_string[-7:-2])
        build_number = ''.join(content_string[-7:-2])
        return directory + build_number
        pass
    except FileNotFoundError:
        print('The file build.properties did not exist in the specified path: ', property_file)
        pass


pass


def check_product_installation(self):
    """Renames the Fiorano Home in the passed directory argument if exists
    
        This Function takes the directory as an argument and searches for Fiorano_home there. If Fiorano_Home exists, it
        calls get_build_number function to get build number to append to the Fiorano. If not, does nothing by throwing 
        an error"""
    try:
        os.chdir(installation_directory)
        directory_list = os.listdir(installation_directory)
        if directory_list.count('Fiorano') == 0:
            print('Fiorano Installation did not exist in the specified directory')
        else:
            print('Found Fiorano directory')
            new_directory = get_build_number(installation_directory)
            os.rename('Fiorano', new_directory)
            print('Renamed the existing Installation directory to ', new_directory)
            pass
        pass
    except ValueError:
        print('Passed String is not of String type')
        pass
    except OSError:
        print('Passed installation_directory  is not valid for the Platform')
        pass
    except TypeError:
        print('The Fiorano is just an directory with no Installation Files. So renaming it to FioranoOld')
        os.rename('Fiorano', 'FioranoOld')
        pass


pass

if __name__ == "__main__":
    check_product_installation(sys.argv[1])
    pass
