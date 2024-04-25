# yl22
# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. 
# Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

import random

""" 1 == "Kivi"
2 == "Paber"
3 == "Käärid" """

computer_choice = random.randint(1,3)

user_choice = int(input("Vali kas 1 (kivi), 2 (paber) või 3 (käärid) "))

if computer_choice < user_choice:
    print("Kasutaja võitis")
elif user_choice < computer_choice:
    print("Arvuti võitis")
else: print("Viik")