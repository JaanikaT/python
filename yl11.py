# yl11
# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

word = input("Sisesta üks seitsmetäheline või pikem sõna: ").strip()

if len(word) >= 7 and len(word)%2 == 1:
    middle = len(word) // 2;
    print(word[middle-1], word[middle], word[middle+1]);
    # print(word[middle-1:middle+2])
elif len(word) <= 7:
    print("Sisesta pikem sõna, sinu antud sõnas on ainult " + str(len(word))+ " tähte.")
else:
    print("Tähti peaks olema paaritu arv")





