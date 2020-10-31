#guess the secret number

import random
import json
import datetime

secret = random.randint(1,30)
attempts = 0
current_time = datetime.datetime.now()
w_attempts = 0

with open('score.txt', 'r') as score_file:
    score_list = json.loads(score_file.read())
    print('Top scores: ' + str(score_list))

print(score_list)
print(score_list[:1])

with open("wrong_guesses.txt", "r") as wrong_file:
    wrong_list = json.loads(wrong_file.read())
    print("Wrong scores: " + str(wrong_file))

print(wrong_list)
print(wrong_list[:1])


uporabnisko_ime = input("Vnesite vase ime: ")

while True:
    guess = int(input("What is your number? "))
    attempts += 1


    if secret == guess:
        print("You have lucky! That's the secret number!")
        print("attempts needed ", str(attempts))
        #zapisovanje v datoteko
        score_list.append(attempts)
        score_list.append({"attempts": attempts, "ime_igralca:": uporabnisko_ime, "date": str(datetime.datetime.now())})

        with open("score.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break

    elif guess > secret:
        w_attempts += 1
        print("Sorry! The number is not correct. Try something smaller.")
        # zapisovanje v datoteko
        wrong_list.append({"wrong answers": w_attempts, "ime_igralca": uporabnisko_ime, "date": str(datetime.datetime.now())})

        with open("wrong_guesses.txt", "w") as wrong_file:
            wrong_file.write(json.dumps(wrong_list))

    elif guess < secret:
        w_attempts += 1
        print("Sorry! The number is not correct. Try something bigger.")
        # zapisovanje v datoteko
        wrong_list.append({"wrong answers": w_attempts, "ime_igralca": uporabnisko_ime, "date": str(datetime.datetime.now())})

        with open("wrong_guesses.txt", "w") as wrong_file:
            wrong_file.write(json.dumps(wrong_list))
