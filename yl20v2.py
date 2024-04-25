# yl20
# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

multiplier = int(input("Sisesta kordaja: "))

# x = x = range(13)   while i in x:
i = 0

while i < 13:
    sum = multiplier * i
    print(str(multiplier) + " x " + str(i) + " = " + str(sum))
    i+=1
