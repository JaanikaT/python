""" yl25

Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
Muuda magustoidu väärtust.
Tee kordus üle dictionary ja väljasta kõik võtmed.
Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
Kontrolli, kas isikukood on dictionary's olemas.
Leia dictionary suurus (elementide arv).
Lisa element enda pikkuse jaoks.
Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
Tutvu kõigi dictionary meetoditega.
Läbi ülesanne juhendi lõpus.
https://www.w3schools.com/python/python_dictionaries.asp
"""
my_dict = {
    "first_name": "Lossi",
    "last_name": "Vaim",
    "birth_year": "1800",
    "living_place": "Kuressaare loss",
    "dessert": "Mõnus maius",
}

# väljasta elukoht .get() (saab panna .get(keyname, value) - value tagastatakse kui keyd ei leia)
home = my_dict.get("living_place")
print (home)
# väljasta elukoht muul viisil
place = my_dict["living_place"]
print("Teistmoodi elukoht: ", place)

# muuda magustoitu
my_dict["dessert"] = "Olde Hansa mandlid"
print("Uus lemmik: ", my_dict["dessert"])

# Tee kordus üle dictionary ja väljasta kõik võtmed
print("Võtmed: ")
for x in my_dict:
    print(x)
# või
print("Võtmed teistmoodi: ")
for x in my_dict.keys():
    print(x) 

# Tee kordus üle dictionary ja väljasta kõik väärtused
print("Väärtused: ")
for y in my_dict:
  print(my_dict[y])
# või
print("Väärtused teistmoodi: ")
for y in my_dict.values():
    print(y)

# Kõik key:value paarid saab välja tuua, väljastab paarid tuple-dena listi sees
# all = my_dict.items()
# print("Kõik paarid:", all)

# Kontrolli, kas isikukood on dictionary's olemas
if "national_id" in my_dict:
    print("Isikukood on olemas")
else: print("Isikukoodi pole")
# saab ka nii:
PIN = my_dict.get("national_id", "pole")
print(PIN)

# Leia dictionary suurus (elementide arv)
print(len(my_dict))

# Lisa element enda pikkuse jaoks.
my_dict["height"] = "2.55"
# või nii:
my_dict.update({"weight": "0.5 kg"})

#Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
#Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
#Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.

# my_dict.pop("birth_year")
# või 
del my_dict["birth_year"]
print(my_dict)

# NB! Tähtis on, et del dict [] sees on ka key-element, mida kustutada, muidu kustutab kogu dict
# my_dict.clear() teeb dict tühjaks, tulemus on {}


# dict.fromkeys(key, value) - teeb uue paari mitmest elemendist
# dict.setdefault(keyname, value) - otsib kas nt "birth_date" olemas; kui on olemas, ei muuda, kui pole, paneb value asemele