from producto import Producto

mochila = Producto("Mochila", 18.9, 3)

print("Total de la mochila:", mochila.total)

mochila.stock = 10
print("Total con stock 10:", mochila.total)

try:
    mochila.stock = -5
except ValueError as mensaje_error:
    print("Error:", mensaje_error)

try:
    mochila.total = 100
except AttributeError as mensaje_error:
    print("Error:", mensaje_error)