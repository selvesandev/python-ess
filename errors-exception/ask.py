def ask_for_int():
    try:
        result = int(input('Please provide num 1')) + int(input('Please provide num 2'))
    except ValueError:
        print('You should provide only number')
    else:
        print(f'The result is {result}')
    finally:
        print('Program completed')


ask_for_int()
