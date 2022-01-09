
import csv
import hashlib
import Fonctions

tab=[]
with open('Liste_Atrouver.csv', newline='',encoding='utf8') as csvfile:
    a = csv.reader(csvfile, delimiter=';')
    for i in a:
        tab.append(i)
tab.pop(0)
for i in tab:
    print("******")
    print(Fonctions.crack_animals(i))
    print(Fonctions.import_chiffre(i))    
