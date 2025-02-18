while True:
    try:
        grade = float(input('Enter the grade you want to transfer to American grades: '))

        if grade < 0 or grade > 10:
            print('Please choose a number between 0 and 10 and try again')
        elif grade >= 8.5:
            print('A')
            break
        elif grade >= 7.5:
            print('B')
            break
        elif grade >= 6.5:
            print('C')
            break
        elif grade >= 5.5:
            print('D')
            break
        elif grade <= 5:
            print('F')
            break
    except:
        print('Please Enter numbers and try again')