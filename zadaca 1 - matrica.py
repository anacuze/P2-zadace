import random
matrica=[]
for i in range(7):
    red=[]
    for j in range(7):
        broj=random.randint(1,9)
        red.append(broj)
    matrica.append(red)
print("Matrica 7x7:")
for red in matrica:
    print(red)
zbroj_rubova=0
for i in range(7):
    for j in range(7):
        if i==0 or i==6 or j==0 or j==6:
            zbroj_rubova+=matrica[i][j]
print("Zbroj elemenata na rubovima:",zbroj_rubova)
