##########################################################################################################################
#######################1 možna rešitev naloge#############################################################################

# CSI investigation - who ate ice cream

# suspects
# Eva
# gender: female
# race: white
# hair color: blonde
# eye color: blue
# face shape: oval

# Larisa
# gender: female
# race: white
# hair color: brown
# eye color: brown
# face shape: oval

# Matej
# gender: male
# race: white
# hair color: black
# eye color: blue
# face shape: oval

# Miha
# gender: male
# race: white
# hair color: brown
# eye color: green
# face shape: square

# human charasteristics
# hair color
black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blonde_hair = "TTAGCTATCGC"

# facial shape
square_face = "GCCACGG"
round_face = "ACCACAA"
oval_face = "AGGCCTCA"

# eye color
blue_eye = "TTGTGGTGGC"
green_eye = "GGGAGGTGGC"
brown_eye = "AAGTAGTGAC"

# gender
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

# race
white_race = "AAAACCTCA"
black_race = "CGACTACAG"
asian_race = "CGCGGGCCG"

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

if (dna.find(female) != -1) & (dna.find(white_race) != -1) & (dna.find(blonde_hair) != -1) & (dna.find(blue_eye) != -1) & (dna.find(oval_face) != -1):
    print("Sladoled je pojedla Eva.")
elif (dna.find(female) != -1) & (dna.find(white_race) != -1) & (dna.find(brown_hair) != -1) & (dna.find(brown_eye) != -1) & (dna.find(oval_face) != -1):
    print("Sladoled je pojedla Larisa.")
elif (dna.find(male) != -1) & (dna.find(white_race) != -1) & (dna.find(black_hair) != -1) & (dna.find(blue_eye) != -1) & (dna.find(oval_face) != -1):
    print("Sladoled je pojedel Matej.")
elif (dna.find(male) != -1) & (dna.find(white_race) != -1) & (dna.find(brown_hair) != -1) & (dna.find(green_eye) != -1) & (dna.find(square_face) != -1):
    print("Sladoled je pojedel Miha.")
else:
    print("Smartninja je pojedel sladoled.")
    
##########################################################################################################################
#######################2 možna rešitev naloge#############################################################################

# CSI investigation - who ate ice cream
#lastnosti DNK
hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
#lastnosti osumljenih
suspects = {"Eva": ["female", "white", "blonde", "blue", "oval"],
            "Larisa": ["female", "white", "brown", "brown", "oval"],
            "Matej":  ["male", "white", "black", "blue", "oval"],
            "Miha": ["male", "white", "brown", "green", "square"]}
#odpremo DNK file in preberemo
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()
#spremenljivka za osumljenega
suspect = []
#primerjamo posamezne lastnosti, ce se nahajajo v DNK, ter jih shranimo pod osumljenega
for key in gender:
    if gender[key] in dna:
        suspect.append(key)

for key in race:
    if race[key] in dna:
        suspect.append(key)

for key in hair_color:
    if hair_color[key] in dna:
        suspect.append(key)

for key in eye_color:
    if eye_color[key] in dna:
        suspect.append(key)

for key in facial_shape:
    if facial_shape[key] in dna:
        suspect.append(key)
#primerjamo lastnosti osumljenih z lastnostmi, ki smo jih dobili pri preverbi posameznih DNK
for i in suspects:
    if suspects[i] == suspect:
        print("Sladoled je pojedel", i)
