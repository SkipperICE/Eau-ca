def afficher_combinaisons():
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                if i != j and i != k and j != k:
                    print(f"{i}{j}{k}", end=", ")
    print()

afficher_combinaisons()