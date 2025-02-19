from time import sleep

while True:
    try:
        number = int(input("Type a number:\n"))
        while True:
            if number > 0:
                number -= 1
                print(number)
                sleep(0.5)
            elif number < 0:
                number += 1
                print(number)
                sleep(0.5)
            else:
                print("Done 👌")
                break
        break
    except ValueError:
        print("Invalid input type a number")