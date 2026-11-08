catalogo = [
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    {"nombre": "Lápiz", "precio": 0.8, "stock": 0},
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
]


def buscar_producto(catalogo, nombre):
    for producto in catalogo:
        if producto["nombre"] == nombre:
            return producto
    raise ValueError("Producto no encontrado")


nombre_buscado = input("¿Qué producto buscas? ")

try:
    producto_encontrado = buscar_producto(catalogo, nombre_buscado)
    print("Producto:", producto_encontrado["nombre"])
    print("Precio:", producto_encontrado["precio"], "€")
    print("Stock:", producto_encontrado["stock"], "unidades")
except ValueError as mensaje_error:
    print("Lo sentimos,", mensaje_error, "- prueba con otro nombre.")