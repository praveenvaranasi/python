def check_product_installation():

    """  Checks Fiorano Product installation
    
        This module checks whether the product Fiorano installation is existed in the Specified directory or not.
        If exists, it moves the existing installation to new folder with SOMETHING appended to newly created folder
        """
    import sys
    try:
        directory, installation_directory = "fiorano",  sys.argv[1]
        print(directory, installation_directory)
        pass
    except ValueError:
        print('Passed String is not of String type')

check_product_installation()





