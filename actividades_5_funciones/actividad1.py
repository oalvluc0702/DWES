catalogo = [
    
{"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    
{"nombre": "Lápiz", "precio": 0.8, "stock": 0},
    
{"nombre": "Mochila", "precio": 18.9, "stock": 3},
]
def prod_mas_caro(catalogo):
    precios =  list()
    for producto in catalogo:
        precios.append(producto["precio"])
    for producto in catalogo:
        if producto["precio"] == max(precios):
            producto_mas_caro = producto
            return producto_mas_caro
stock_agotado= list()
contador = 0
precio_total = 0
for producto in catalogo:
    precio_total+=producto["precio"]
    if not producto["stock"] > 0:
        stock_agotado.append(producto)
        contador+=1
        

print(f"sin stock: {stock_agotado}")
print(f"precio medio: {precio_total / len(catalogo):.2f}")
print(f"el producto mas caro es: {prod}")