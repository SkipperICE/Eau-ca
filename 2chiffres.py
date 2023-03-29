def afficher_combinaisons():
    for i in range(10):
        for j in range(10):
                print(f"{i}{j}", end=", ")
    print()

afficher_combinaisons()


def afficher_combinaisons2():
    for i in range(100):
        for j in range(i+1, 100):
            print(f"{i:02d} {j:02d}", end=", ")
    print()

afficher_combinaisons2()