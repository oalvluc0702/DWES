# Clase base: de ella heredan las otras dos
class ErrorProducto(Exception):
    pass


class NombreVacioError(ErrorProducto):
    pass


class PrecioInvalidoError(ErrorProducto):
    pass


def crear_producto(nombre, precio):
    if nombre.strip() == "":
        raise NombreVacioError("El nombre del producto no puede estar vacío")
    if precio <= 0:
        raise PrecioInvalidoError("El precio debe ser mayor que cero")
    return {"nombre": nombre, "precio": precio}


# 1) Capturando cada excepción por separado
print("--- Capturando por separado ---")

try:
    producto_nuevo = crear_producto("", 10)
    print(producto_nuevo)
except NombreVacioError as mensaje_error:
    print("Error de nombre:", mensaje_error)
except PrecioInvalidoError as mensaje_error:
    print("Error de precio:", mensaje_error)

try:
    producto_nuevo = crear_producto("Cantimplora", -5)
    print(producto_nuevo)
except NombreVacioError as mensaje_error:
    print("Error de nombre:", mensaje_error)
except PrecioInvalidoError as mensaje_error:
    print("Error de precio:", mensaje_error)

try:
    producto_nuevo = crear_producto("Tirita", 12.5)
    print("Producto creado:", producto_nuevo)
except NombreVacioError as mensaje_error:
    print("Error de nombre:", mensaje_error)
except PrecioInvalidoError as mensaje_error:
    print("Error de precio:", mensaje_error)

# 2) Un único except con la clase base
print("--- Capturando con ErrorProducto ---")

try:
    producto_nuevo = crear_producto("", 10)
    print(producto_nuevo)
except ErrorProducto as mensaje_error:
    print("Error al crear el producto:", mensaje_error)

try:
    producto_nuevo = crear_producto("Macuto", -5)
    print(producto_nuevo)
except ErrorProducto as mensaje_error:
    print("Error al crear el producto:", mensaje_error)