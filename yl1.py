# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse 
# ja väljastab ümardatud tulemuse. (round)

eek = input("Sisesta kroonid: ")
eek = float(eek)
eur = round(eek / 15.6466, 2)
print(eur)
