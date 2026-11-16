from producto import Producto, ProductoRebajado, Formacion, total_con_iva


class ServicioPremium:
    def __init__(self, nombre_servicio, precio):
        self.nombre_servicio = nombre_servicio
        self.precio = precio


producto_normal = Producto("Libro", 10, 5)
producto_rebajado = ProductoRebajado("Mochila", 20, 3, 25)
curso_python = Formacion("Python básico", 100)

lista_mezclada = [producto_normal, producto_rebajado, curso_python]
print("Total con IVA:", round(total_con_iva(lista_mezclada), 2), "€")

servicio_premium = ServicioPremium("Soporte 24h", 50)
lista_mezclada.append(servicio_premium) 

try:
    print("Total con IVA:", total_con_iva(lista_mezclada))
except AttributeError as mensaje_error:
    print("Error:", mensaje_error)

# ¿En qué línea salta? -- Dentro de total_con_iva, en la línea
# "total_acumulado = total_acumulado + articulo.precio_con_iva()",
# cuando el bucle llega al servicio premium.
# ¿Por qué no lo vio nadie antes? -- Porque Python no comprueba los métodos
# al definir la clase ni al hacer append, por el duck typing.