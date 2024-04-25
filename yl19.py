# yl19
# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

vowels = ["a","e","i", "o", "u", "õ", "ä", "ö", "ü"]
# vowels = "aeiouõäöü"
# vowels = "a, e, i, o, u, õ, ä, ö, ü".split(",") - tekitab kopeeritud tekstist ise listi nagu esimene
text = (input("Sisesta tekst ")).lower()

count = 0

for char in text: # või text.lower()
    if char in vowels:
        count +=1   
print(count)
    