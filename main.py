def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        try:
            number = int(input('Enter a Number: '))
        except ValueError:
            print ('Invalid Input: Value Must be Numeric')
        else:
            print (number)
            break
                
    
    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
