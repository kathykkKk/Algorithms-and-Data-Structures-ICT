def FizzBuzz (number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end="  ")
    else:
        if number % 3 == 0:
            print("Fizz", end="  ")
        else:
            if number % 5 == 0:
                print("Buzz", end="  ")
            else:
                print(number, end="  ")


for i in range(1, 16):
    FizzBuzz(i)



