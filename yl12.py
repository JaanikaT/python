# yl12
# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp

fruit = ["õun", "banaan", "ploom"]
print(fruit)

print("Esimene puuvili on "+ fruit[0])

fruit2 = fruit + ["nektariin"]
print("Viimane puuvili on " + fruit2[len(fruit2)-1])

fruit2[1] = "astelpaju"
print(fruit2)

for i in fruit2:
    if i == "õun":
        print("õun on olemas")
    #Kuidas teha, et else "Seda puuvilja pole listis" Ei prindiks 4x (nt pirn)

print("Elemente on", len(fruit2))

del fruit2[3]
print(fruit2)

#kindla väärtusega element: fruit2.remove("ploom") või
#koha järgi fruit2.pop(1) -eemaldab teise elemendi fruit2.pop() tühjalt eemaldab viimase

fruit2.reverse()

fruit2.sort()
print("Tähestiku järjekorras", fruit2)
