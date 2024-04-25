# yl13
# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline ilist - multi dimensional)

user_pet = input("Sisesta lemmikloom: ")
pet_abc = list(user_pet)
print(pet_abc[0])

pet_list = ["kuldkala", "hamster", "papagoi"] 
pet_list.append(user_pet)

print(pet_list)
print(pet_list[-1][-1])

#viimase elemendi kaks viimast tähte
print(pet_list[-1][-2::])

print(pet_list[-1][-1:-3:-1])
