import datetime
import json
import random

def get_score_list():
    with open("score.txt", "r") as score_file:
        score_list = json.load(score_file.read())
        return(score_list)

def top_scores():
    return (get_score_list())
    print("Top scores: " + str(get_score_list()))
    for score_dict in get_score_list():
        return(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

def play_game():
    secret = random.randint(1, 30)
    level = input("Enter your level 'H' - hard or 'E' - easy: ")
    def play_game_level(level):
        if level == "H":
            return ("Wrong guess. Try again!")
        elif level == "E" and guess > secret:
            return ("Try something smaller.")
        else:
            return ("Try something bigger.")

    while True:
        attempts = 0
        guess = int(input("Guess the secret number (between 1 and 30): "))
        if guess == secret:
            score_list = get_score_list()
            attempts += 1
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
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

attempts = 0

while True:
    selection = input("Would you like to A - play a game, B - see the best scores or C - quit?")
    if selection == "A":
        play_game()
    if selection == "B":
        print(top_scores())
    else:
        break
