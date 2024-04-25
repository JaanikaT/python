# yl7
# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)

a = int(input("Sisesta täisarv "))
if a % 2:
    print(a, "on paaritu arv")
else:
    print(a, "on paarisarv")      