def welcome():
     print('''
    Welcome to Calculator 
    ''')
    
welcome()
def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for mulitplication
    / for division
    ''')



    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))


    # Addittion
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')



    welcome()
    def again():
        calc_again = input('''
        Do you want to calculate again?
        Please type Y for YES and N for NO.
        ''')

        if calc_again.upper() == 'Y':
            calculate()

        elif calc_again.upper() == 'N':
            print('See you next time.')

        else:
            again()

    again()
calculate()

