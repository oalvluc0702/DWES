# Predicción: ValueError (int no entiende un texto con decimal)
try:
    numero = int("3.5")
except ValueError as mensaje_error:
    print("int('3.5') -> ValueError:", mensaje_error)

# Predicción: IndexError (la lista solo tiene posiciones 0 y 1)
try:
    elemento = [1, 2][5]
except IndexError as mensaje_error:
    print("[1, 2][5] -> IndexError:", mensaje_error)

# Predicción: KeyError (la clave no existe en el diccionario vacío)
try:
    valor = {}["x"]
except KeyError as mensaje_error:
    print("{}['x'] -> KeyError:", mensaje_error)

# Predicción: TypeError (no se puede sumar texto y número)
try:
    resultado = "a" + 1
except TypeError as mensaje_error:
    print("'a' + 1 -> TypeError:", mensaje_error)

# Predicción: ZeroDivisionError (no se puede dividir entre cero)
try:
    resultado = 1 / 0
except ZeroDivisionError as mensaje_error:
    print("1 / 0 -> ZeroDivisionError:", mensaje_error)

# Predicción: ValueError (Python solo acepta el punto como separador, no la coma)
try:
    numero_decimal = float("1,5")
except ValueError as mensaje_error:
    print("float('1,5') -> ValueError:", mensaje_error)