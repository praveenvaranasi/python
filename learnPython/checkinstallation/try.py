def try_rename_mechanism(buid_number):
    directory_list=['Fiorano','Fiorano10400','Fiorano104001','Fiorano104002']
    if directory_list.count('Fiorano') != 0:
        res = 'Fiorano' + build_number
        if directory_list.count(res) != 0:
            res = res + '1'
            print(res)
            if directory_list.count(res) != 0:
                # print(res[7:])
                list = str(res.split(","))
                print("length is: ",len(list))
                list[-3] = int(res[-3]) + 1
                for i in list:
                    print(i, end=",")
                    pass
                #''.join(list)
                #print(list)
                pass
        pass

    #print(build_number)
    pass

if __name__ == "__main__":
    build_number = input('Enter the build number:\n')
    try_rename_mechanism(build_number)
    pass