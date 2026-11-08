from producto import Producto

filas_del_catalogo = ["Mochila,18.9,3", "Lápiz,0.8,100", "Cuaderno,2.5,12"]

catalogo = []
for fila in filas_del_catalogo:
    producto_nuevo = Producto.desde_fila(fila)
    catalogo.append(producto_nuevo)

for producto in catalogo:
    print(producto)
    print("¿Es un Producto?", isinstance(producto, Producto))