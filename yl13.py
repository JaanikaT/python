# yl13
# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline ilist - multi dimensional)

user_pet = input("Sisesta lemmikloom ")
pet_abc = list(user_pet)
print(pet_abc[0])

pet_list = ["kuldkala"],["hamster"],["papagoi"] + [user_pet]
 # vist ei lisa päris õigesti?

print(pet_list)
print(pet_abc[len(pet_abc)-1])
# kuna on ette teada, et viimane on kasutaja lisatud element