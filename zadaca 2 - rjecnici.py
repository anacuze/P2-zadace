imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

import random
ocjene=[]

for ime in imena:
    ocjena=random.randint(1,5)
    ocjene.append(ocjena)
brojac={}

for ocjena in ocjene:
    brojac[ocjena]=brojac.get(ocjena,0)+1
print("Broj ocjena po vrijednosti:")
print(brojac)
prolazni=0

for ocjena in ocjene:
    if ocjena>1:
        prolazni+=1
        
ukupno=len(ocjene)
postotak=(prolazni/ukupno)*100

print("Ukupno studenata:",ukupno)
print("Broj studenata koji su prosli:",prolazni)
print("Postotak prolaznosti:",postotak,"%")
