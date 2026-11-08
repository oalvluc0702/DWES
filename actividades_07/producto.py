class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio        # pasa por el setter
        self.stock = stock          # pasa por el setter

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = nuevo_stock

    @property
    def total(self):
        return self.precio * self.stock

    @property
    def etiqueta(self):
        return f"{self.nombre} ({self.stock} uds.)"

    @classmethod
    def desde_fila(cls, fila):
        nombre, precio_texto, stock_texto = fila.split(",")
        return cls(nombre, float(precio_texto), int(stock_texto))

    def vender(self, unidades):
        if unidades > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock = self.stock - unidades

    def precio_con_iva(self, tipo_iva=0.21):
        return round(self.precio * (1 + tipo_iva), 2)

    def __str__(self):
        return f"{self.nombre}: {self.precio:.2f} € ({self.stock} uds.)"

    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio}, {self.stock})"

    def __eq__(self, otro_producto):
        if not isinstance(otro_producto, Producto):
            return False
        return (self.nombre == otro_producto.nombre
                and self.precio == otro_producto.precio)


class ProductoRebajado(Producto):
    def __init__(self, nombre, precio, stock, porcentaje_descuento):
        super().__init__(nombre, precio, stock)
        self.porcentaje_descuento = porcentaje_descuento

    def precio_con_iva(self, tipo_iva=0.21):
        precio_rebajado = self.precio * (1 - self.porcentaje_descuento / 100)
        return round(precio_rebajado * (1 + tipo_iva), 2)


class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock, tamano_mb):
        super().__init__(nombre, precio, stock)
        self.tamano_mb = tamano_mb


class Formacion:
    def __init__(self, nombre_curso, precio):
        self.nombre_curso = nombre_curso
        self.precio = precio

    def precio_con_iva(self, tipo_iva=0.21):
        return round(self.precio * (1 + tipo_iva), 2)


class LineaPedido:
    def __init__(self, producto, unidades):
        self.producto = producto
        self.unidades = unidades

    def subtotal(self):
        return self.producto.precio * self.unidades

    def __str__(self):
        return f"{self.unidades} x {self.producto.nombre} = {self.subtotal()} €"

    def __repr__(self):
        return f"LineaPedido({self.producto!r}, {self.unidades})"


def total_con_iva(lista_de_articulos):
    total_acumulado = 0
    for articulo in lista_de_articulos:
        total_acumulado = total_acumulado + articulo.precio_con_iva()
    return total_acumulado