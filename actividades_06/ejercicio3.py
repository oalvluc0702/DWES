def aplicar_descuento(precio, porcentaje):
    if precio <= 0:
        raise ValueError("El precio debe ser positivo")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)


# error del precio
try:
    precio_con_descuento = aplicar_descuento(-50, 10)
    print(precio_con_descuento)
except ValueError as mensaje_error:
    print("Error en el precio:", mensaje_error)

# error del porcentaje
try:
    precio_con_descuento = aplicar_descuento(100, 150)
    print(precio_con_descuento)
except ValueError as mensaje_error:
    print("Error en el porcentaje:", mensaje_error)

# correcta
try:
    precio_con_descuento = aplicar_descuento(100, 20)
    print("Precio con descuento:", precio_con_descuento)
except ValueError as mensaje_error:
    print("Error:", mensaje_error)