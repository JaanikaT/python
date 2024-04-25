# yl21
# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random

computer_no = random.randint(0, 100) # random.randrange(0,101)

user_no = int(input("Paku arv 0-100ni "))

while computer_no != user_no:
    if computer_no > user_no:
        print("Mu arv on suurem")
    else: print("Mu arv on väiksem")
    user_no = int(input("Paku uuesti "))
    
else:
    print("Arvasid õigesti, mu arv oligi " + str(computer_no))   

#print(computer_no)
    
""" # while computer_no != user_no:
    if computer_no > user_no:
        print("Mu arv on suurem")
    elif user_no > computer_no:
    print("Mu arv on väiksem")
    user_no = int(input("Paku uuesti "))
    
else:
    print("Arvasid õigesti, mu arv oligi " + str(computer_no))
 """