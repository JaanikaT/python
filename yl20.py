# yl20
# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

""" b = ""

while not b.isnumeric():
    b = input("Sisesta tegur: ")

 """

b = input("Sisesta arv ")
while b.isnumeric() != True:
    b = input("Sisesta arv, mitte sõna ")  #---- Ei saa kasutada, sest teeb ainult 2 korda

b = int(b)

for a in range(0, 13):
    print(b, "x", a, "=", a*b )

# x = range(13)

# i = 0

# while i in x:
#     sum = 8*i
#     print("8 x " + str(i) + " = " + str(sum))
#     i+=1
