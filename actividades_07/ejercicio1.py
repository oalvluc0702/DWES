from producto import Producto, LineaPedido

cuaderno = Producto("Cuaderno", 2.5, 12)
lapiz = Producto("Lápiz", 0.8, 100)
mochila = Producto("Mochila", 18.9, 3)

pedido = [
    LineaPedido(cuaderno, 2),
    LineaPedido(lapiz, 10),
    LineaPedido(mochila, 1),
]

total_pedido = 0
for linea in pedido:
    total_pedido = total_pedido + linea.subtotal()
print("Total del pedido:", total_pedido, "€")

print(cuaderno)         # print usa __str__
print(repr(cuaderno))   # repr() usa __repr__
print(pedido[0])        # print usa __str__ de LineaPedido
print(pedido)           # una lista muestra el __repr__ de cada elemento
