from math import sqrt
from operaciones import sqrt as sqrt_operaciones
productos = [
{"nombre": "Mochila", "precio": 18.9},
    
{"nombre": "Cuaderno", "precio": 2.5},
    
{"nombre": "Lápiz", "precio": 0.8},
]

def saludar():
    print("hola")
    
ordenados = sorted(productos, key=lambda prod: prod["precio"])
doble = list(map(lambda p:p['precio']*2, productos))
print(doble)

print(sqrt_operaciones(2))

if __name__ == "__main__":
    print("se esta ejecutando correctamente")
    saludar()