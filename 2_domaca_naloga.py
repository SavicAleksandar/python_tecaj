###########################################
# domača naloga 2.1 - pretvorba km v milje:

print("Pozdravljen! V tem programu pretvarjamo kilometre v milje.") #opis programa
km = float(input("Vpiši željeno število kilometrov, ki jih želiš pretvoriti v milje: "))    #vnos vrednosti

milja = float(km * 0.621)   #pretvorba vrednosti

print('Pretvorba je ', milja, 'milj') #izpis pretvorjene vrednosti

while True: #zanka kjer uporabnika vprašamo po ponovni pretvorbi

    pogoj = input('Ali želiš še eno pretvorbo? Odgovori z DA ali NE. ')
    pogoj = pogoj.lower() #spremenimo pogoj v majhne crke

    if pogoj == "da":   #if stavek s pogoji
        km = float(input("Vnesi število km: "))
        milja = float(km * 0.621)
        print('Pretvorba je ', milja, 'milj')
    elif pogoj == "ne":
        print('Hvala za uporabo programa.')
        break
    else:
        print("Napačen odgovor!")

##############################
#domača naloga 2.2 - FizzBuzz:

x = int(input("Vnesi število med 1 in 100: "))  #vnos poljubnega števila med 1 in 100

if x < 100:
    x = x + 1   #številu prištejemo +1, saj for zanka začne šteti pri 0

    for i in range(1, x):   #štejemo od 1 naprej
        if i % 3 == 0 & i % 5 ==0:      #primerjamo prvo in drugo število, če je ostanek enak 0
            print("fizzbuzz")
    elif i % 3 == 0:
        print("buzz")
    elif i % 5 == 0:
        print("fizz")
    else:
        print(i)
else:
    print("Stevilo je vecje kot 100.")

###############################
#domača naloga 2.3 - lowercase:

text = str(input("Napiši tekst: ")) #vpišemo tekst
text = text.lower() #vse crke spremenimo v majhne tiskane
print("Tekst napisan z majhnmi crkami: ", text) #izpisan tekst
