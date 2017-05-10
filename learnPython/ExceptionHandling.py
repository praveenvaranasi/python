def Exception():
    try:
        A = int(input('Enter the Value of the variable A\n'))
        B = int(input('Enter the Value of the variable B\n'))
        print('Dividing A by B')
        result = A // B
        print (result)
    except ZeroDivisionError:
        print('you have Entered B value Zero. Please try something else')
    except ValueError:
        print('Only integer values are accepted. Dont enter other than Strings.')
    finally:
        print('understood!!')

Exception()
