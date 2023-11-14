# yl11
# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

word = input("Sisesta üks seitsmetäheline või pikem sõna: ").strip()

if len(word) >= 7 and len(word)%2 != 0:
    middle = len(word) // 2;
    print(list(word))
    
    # print(middle);
else:
    print("Sisesta pikem sõna, sinu antud sõnas on ainult" + len(word)+ "tähte.")





