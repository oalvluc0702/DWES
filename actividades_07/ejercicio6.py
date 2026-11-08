from producto import (Producto, ProductoRebajado, ProductoDigital,
                      Formacion)

lista_de_articulos = [
    Producto("Libro", 10, 5),
    ProductoRebajado("Mochila", 20, 3, 25),
    Formacion("Python básico", 100),
    ProductoDigital("Libro digital", 10, 50, 15),
]

for articulo in lista_de_articulos:
    print(type(articulo).__name__,
          "| ¿Producto?", isinstance(articulo, Producto),
          "| ¿ProductoRebajado?", isinstance(articulo, ProductoRebajado),
          "| precio con IVA:", articulo.precio_con_iva())

# Producto: usa su propia versión.
# ProductoRebajado: usa la suya, que sobrescribe la del padre.
# Formacion: usa la suya.
# ProductoDigital: no la define, así que usa la de Product.