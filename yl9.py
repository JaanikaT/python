# yl9
# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input("Sisesta esimese külje pikkus "))
b = float (input("Sisesta teise külje pikkus "))
c = float(input("Siseta kolmanda külje pikkus "))

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print("Kokku ei tule kolmnurk")
    
elif a == b == c:
    print("Kolmnurk on võrdkülgne")
elif a == b or a == c or b ==c:
    print("Kolmnurk on võrdhaarne")
else:
    print("Kolmnurk on erikülgne")
