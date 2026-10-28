nota = int(input("Dime una nota entera"))
if nota < 5:
    print("Insuficiente")
elif nota <= 6:
    print("suficiente")
elif nota == 7:
    print("bien")
elif nota <= 9:
    print("Notable")
else:
    print("Sobresaliente")

linea = "insuficiente" if nota < 5 else "suficiente" if nota <= 6 else "Bien" if nota == 7 else "Notable" if nota <= 9 else "Sobresaliente"

print(linea)

    