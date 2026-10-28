lista = ["Cuaderno", "Lápiz", "Mochila","Agua"]
acumulador = 0
for posicion, material in enumerate(lista):
    acumulador+=1
print(f"Hay un total de: {acumulador} productos")