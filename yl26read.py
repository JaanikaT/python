import csv

with open("yl26_data.txt","r") as data:
    lines = (data.read().split("\n"))
    print(lines)
    revenue = {}
    expences = {}

    for line in lines:
        if line.startswith('        '):
            names = line.split('    ')[-1]
            names = names.split(' ')
            # siin peab kaotama k6ik elemendid, mis on lyhemad kui 1 char
            for element in names:
                if len(element) <2:
                    names.remove(element)

