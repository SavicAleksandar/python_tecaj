#domača naloga 1.1: mood checker

mood = input("What is your mood? ")

mood = mood.lower()   #vse crke v besedi spremenimo v majhne

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times")
elif mood == "sad":
    print("Dont be sad. Be happy!")
elif mood == "excited":
    print("Why?")
elif mood == "relaxed":
    print("Lucky one!")
else:
    print("I dont recognize this mood")

#domača naloga 1.2: guess the secret number

secret = 21
guess = int(input("What is your number? "))

if secret == guess:
    print("You have lucky! That's the secret number!")
else:
    print("Sorry! The number is not correct.")

#domača naloga 1.3: calculator

nm1 = float(input("Type the first number: "))   #float, ker se lahko pojavljajo številke z decimalkami pri deljenju
nm2 = float(input("Type the second number: "))

op = input("Type the operator +, -, * or /: ")

if op == "+":
    print("The sum of numbers is: ", nm1 + nm2)
elif op == "-":
    print("The substracion of numbers is: ", nm1 - nm2)
elif op == "*":
    print("The multiplication of numbers is: ", nm1 * nm2)
elif op == "/":
    print("The division of numbers is: ", nm1 / nm2)
else:
    print("This operator does not exist. ")
