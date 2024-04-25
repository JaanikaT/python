# yl10
# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, 
# küsib kasutajalt vanuse, 
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, 
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, 
# kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

name = input("Sisesta oma nimi: ").capitalize()
print("Tere,", name + "!")

place = input("Sisesta elukoha maakond: ").lower()

if place == "saaremaa": # või if place.lower() ==
    print("Ahoi, saarlane!")

# if place == "Saaremaa" or "saaremaa" - pole vahet, mida kirjutad nt hiiumaa loetakse (saaremaaks) vastus alati True,  
# ehk väljastab midagi PEAB KIRJUTAMA kaks korda!! if place == "Saaremaa" or place == "saaremaa" , siis kontrollib ainult saaremaad

# if "saaremaa" in location -> see töötab ka kui kirjutada saaremaa ja hiiumaa jne

age = int(input("Sisesta oma vanus: "))

if age < 18:
    print("Oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Võid autot juhtida.")