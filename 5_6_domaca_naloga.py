import random

while True:
    countries_capitals = {"Austria": "Vienna", "Croatia": "Zagreb", "Hungary": "Budapest", "Slovenia": "Ljubljana",
                          "Italy": "Rome"}
    country = random.choice(list(countries_capitals)) #izbere nakljucno drzavo

    for i in countries_capitals:    #najdemo glavno mesto glede na doloceno drzavo
        if i == country:
            capital = countries_capitals[i]

    quess = input("What is the capital of " + country +"? ") #igralca povprasamo za glavno mesto drzave

    if quess == capital: #primerjamo ali odgovor ustreza
        print("Bravo! You guess the capital of " + country)
        break
    else:
        print("Sorry! The answer is not correct.")
