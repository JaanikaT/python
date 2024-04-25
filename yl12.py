# yl12
# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp

# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
fruit = ["õun", "banaan", "ploom"]
print(fruit)

# Väljasta listi esimene väärtus
print("Esimene puuvili on "+ fruit[0])

# Lisa listi lõppu uus puuvili
fruit2 = fruit + ["nektariin"]

# Väljasta listi viimane väärtus
print("Viimane puuvili on " + fruit2[len(fruit2)-1]) # print("Viimane puuvili on " + fruit2[-1])

# Muuda ühe elemendi väärtust ja väljasta kogu list
fruit2[1] = "pirn"
print(fruit2)

# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
i = input("Kontrolli puuvilja ")
if i in fruit2:
    print(i + " on olemas")
else: print(i + " pole listis")    

# Väljasta listi pikkus
print("Elemente on", len(fruit2))

# Eemalda listist element ja väljasta kogu list
del fruit2[3]
print(fruit2)

#kindla väärtusega element: fruit2.remove("ploom") või
#koha järgi fruit2.pop(1) -eemaldab teise elemendi fruit2.pop() tühjalt eemaldab viimase

# Muuda listi järjekord vastupidiseks
fruit2.reverse()

# Sorteeri list ja väljasta

#fruit2.sort() meetod - muudab originaali ära
print(sorted(fruit2)) 
# funktsioon - ei muuda originaali, tagastab uue listi
print(fruit2)
