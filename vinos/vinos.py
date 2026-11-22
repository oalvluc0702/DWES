vinos_jerez = [
    "Sherry Classic",
    "Vino Blanco",
    "Fino SHERRY",
    "Moscatel",
    "ShErry Cream"
]
import pprint as p
def contiene_sherry(vino: str) -> bool:
    """Comprueba si el nombre de un vino contiene 'sherry', sin distinguir mayúsculas.

    Parámetros:
        vino: nombre del vino.

    Devuelve:
        True si el nombre contiene 'sherry', False si no.
    """
    vino_formateado = vino.strip().lower()
    return "sherry" in vino_formateado

def obtener_vinos(vinos_jerez: list[str]) -> tuple[dict,list[str]]:
    """Analiza una lista de vinos y detecta cuáles contienen 'sherry'.

    Parámetros:
        vinos_jerez: lista con los nombres de los vinos.

    Devuelve:
        Una tupla con un diccionario (nombre del vino -> True/False según
        contenga 'sherry') y una lista, obtenida con filter(), solo con
        los vinos que lo contienen.
    """
    diccionario_vinos = {}
    for vino in vinos_jerez:
        diccionario_vinos[vino] = contiene_sherry(vino)
    
    lista_vinos_sherry = list(filter(contiene_sherry,vinos_jerez))
    return diccionario_vinos,lista_vinos_sherry
if __name__ == "__main__":
    diccionario, lista_sherry = obtener_vinos(vinos_jerez)

    print("Diccionario de vinos:")
    p.pprint(diccionario, sort_dicts=False)

    print("\nLista de vinos con 'Sherry':")
    p.pprint(lista_sherry)