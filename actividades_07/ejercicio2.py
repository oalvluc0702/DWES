from producto import Producto

camiseta = Producto("Camiseta", 12.0, 5)

camiseta.vender(2)
print("Stock tras vender 2:", camiseta.stock)

try:
    camiseta.vender(10)
except ValueError as mensaje_error:
    print("Error:", mensaje_error)

print("Stock final:", camiseta.stock)