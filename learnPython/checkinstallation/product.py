class Check:

    def check_product_installation(self):

        """  Checks Fiorano Product installation
    
        This module checks whether the product Fiorano installation is existed in the Specified directory or not.
        If exists, it moves the existing installation to new folder with SOMETHING appended to newly created folder
        """
    import sys
    import os
    try:
        directory, installation_directory = "Fiorano",  sys.argv[1]
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


def get_build_number():
    pass






