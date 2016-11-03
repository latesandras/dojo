#dojo 

number1 = input("Enter a number, please!")
number = int(number1)

if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
    quit()

if number%3 == 0:
    print ("Fizz")
    quit()

if number%5 == 0:
    print ("Buzz")
    quit()