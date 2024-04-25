# yl8
# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

year = int(input("Sisesta aastaarv "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    # kui kasutada prindis +, siis on vaja, et mõlemad on ühte tüüpi andmed e siinjuhul stringid, 
    # NB! vaja tühik vahele jätta

    print(str(year) + " on liigaasta")

    # kui kasutada , siis saab erinevaid andmetüüpe kasutada ja tühik jääb ise vahele
else:
    print(year, "on lihtaasta")