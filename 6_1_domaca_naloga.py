#domaca naloga 6.1

#navodila - uporabniski vnos kosarkasa in nogometasa
#uporabnik vpise datum, ki ga je trreba shraniti v tekstovno datoteke

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2,
                          rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)


print(lebron.first_name)
print(lebron.height_cm)

print(kev_dur.last_name)
print(kev_dur.rebounds)

bball_players = [lebron, kev_dur]

for player in bball_players:
    print(player.last_name + ", " + player.first_name)


# dictionary
lebron_dict = {"first_name": "Lebron", "last_name": "James", "height_cm": 203, "weight_kg": 113, "points": 27.2,
               "rebounds": 7.4, "assists": 7.2}

print(lebron_dict["first_name"])
print(lebron_dict["height_cm"])


# converting kg to lbs
print(lebron.weight_to_lbs())
print(kev_dur.weight_to_lbs())


# football
ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                         yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575,
                       yellow_cards=67, red_cards=0)

#vnesi podatke igralca
print("Vnesi podatke kosarkasa.")
name = input("Vnesi ime igralca: ")
l_name = input("Vnesi priimek igralca: ")
visina = input("Vnesi visino igralca: ")
teza = input("Vnesi tezo igralca: ")
tocke = input("Vnesi tocke igralca: ")
skoki = input("Vnesi skoke igralca: ")
asistenca = input("Vnesi asistence igralca: ")

novi_igralec_k = BasketballPlayer(first_name = name, last_name = l_name, height_cm = visina, weight_kg = teza, points = tocke, rebounds = skoki, assists = asistenca)

print("Vnesi podatke nogometasa.")
name = input("Vnesi ime igralca: ")
l_name = input("Vnesi priimek igralca: ")
visina = input("Vnesi visino igralca: ")
teza = input("Vnesi tezo igralca: ")
goli = input("Vnesi gole igralca: ")
rumeni_kartoni = input("Vnesi rumene kartone igralca: ")
rdeci_kartoni = input("Vnesi rdece kartone igralca: ")

novi_igralec_n = FootballPlayer(first_name = name, last_name = l_name, height_cm= visina, weight_kg= teza, goals= goli, yellow_cards= rumeni_kartoni, red_cards= rdeci_kartoni)

with open("kosarkasi.txt", "w") as kosarkasi_file:
    kosarkasi_file.write(str(novi_igralec_k.__dict__))

with open("nogometasi.txt", "w") as nogometasi_file:
    nogometasi_file.write(str(novi_igralec_n.__dict__))

print("Uspesno ste vnesli podatke o kosarkasu: ", novi_igralec_k.__dict__)
print("Uspesno ste vnesli podatke o nogometasu: ", novi_igralec_n.__dict__)
