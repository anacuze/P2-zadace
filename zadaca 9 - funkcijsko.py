def pozdrav(ime):
    print("Pozdrav " + ime + "!")

dobrodosao = lambda ime: print("Dobrodošao " + ime + "!")

def ispisi_dobrodoslicu(poruka):
    poruka("Ana")

ispisi_dobrodoslicu(pozdrav)

ispisi_dobrodoslicu(dobrodosao)
