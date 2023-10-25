# yl6
# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)

a = int(input("Sisesta esimene arv:"))
b = int(input("Sisesta teine arv:"))
c = int(input("Sisesta kolmas arv:"))

if a > b and a > c:
    print("Maksimum on", a)
elif b > c:
    print("Maksimum on", b)
else:
    print("Maksimum on", c)    
    