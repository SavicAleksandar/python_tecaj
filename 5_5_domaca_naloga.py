import datetime
import json
import random

def get_score_list():
    with open("score.txt", "r") as score_file:
        score_list = json.load(score_file)
    return(score_list)

def top_scores():
    score_list = get_score_list()
    result_top3 = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return ("Top 3 scores: ", result_top3)

def play_game():
    attempts = 0
    secret = random.randint(1, 30)
    name = input("What is your name: ")
    level = input("Enter your level 'H' - hard or 'E' - easy: ")
    def play_game_level(level):
        if level == "H":
            print ("Wrong guess. Try again!")
        elif level == "E" and guess > secret:
            print ("Try something smaller.")
        else:
            print ("Try something bigger.")

    while True:
        attempts += 1
        guess = int(input("Guess the secret number (between 1 and 30): "))
        if guess == secret:
            score_list = get_score_list()

            score_list.append({"attempts": attempts, "name": name, "date": str(datetime.datetime.now())})
            with open("score.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print(play_game_level(level))
#            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print(play_game_level(level))
#            print("Your guess is not correct... try something bigger")

while True:
    selection = input("Would you like to A - play a game, B - see the best scores or C - quit?")
    if selection == "A":
        play_game()
    if selection == "B":
        print(top_scores())
    else:
        break
