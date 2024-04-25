# yl14
# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (ext - extension - faili laiend) 
# ja prindib välja laiendi (“ext”). (str.split)

fail = input("Sisesta failinimi kujul failinimi.ext: ")
fail_extension = fail.split(".")

print (fail_extension[-1])

#print(fail.split(".")[-1])