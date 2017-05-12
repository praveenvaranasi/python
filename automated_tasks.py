import sys
import os


class Check:
    directory, installation_directory, version = "Fiorano", sys.argv[1], 11
    property_file = os.path.join(installation_directory, directory, str(version), "build.properties")

    def check_product_installation(self):

        """  Checks Fiorano Product installation

        This module checks whether the product Fiorano installation is existed in the Specified directory or not.
        If exists, it moves the existing installation to new folder with SOMETHING appended to newly created folder
        """

    try:
        os.chdir(installation_directory)
        directory_list = os.listdir(installation_directory)
        for directory_name in directory_list:
            if directory_name == "Fiorano":
                os.rename('Fiorano', 'FioranoOld')
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


class Say(Check):
    check = Check()

    def get_build_number(self):
        try:
            print('It\'s Ok')
            file = open(Check.property_file)
            for line in file.read():
                print(line, end="")
                pass
            file.close()
            pass
        except FileNotFoundError:
            print('The file build.properties did not exist in the specified path: ', Check.property_file)
        pass
    pass
pass


say = Say()

say.get_build_number()









