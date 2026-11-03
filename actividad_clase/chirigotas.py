grupos = {
    "chirigotas": {
        "Los Yesterday": {
            "preliminares": [9.1, 9.3, 9.0, 9.2],
            "cuartos": [9.4, 9.2, 9.1, 9.3],
            "semifinal": [9.6, 9.5, 9.4, 9.5],
            "final": [9.7, 9.6, 9.8, 9.7]
        },
        "Er Chele Vara": {
            "preliminares": [8.5, 8.6, 8.7, 8.9],
            "cuartos": [8.9, 8.8, 8.6, 8.7]
        }
    },
    "comparsas": {
        "Los Ángeles Caídos": {
            "preliminares": [9.5, 9.6, 9.7, 9.8],
            "cuartos": [9.7, 9.6, 9.8, 9.9],
            "semifinal": [9.8, 9.9, 9.8, 9.9],
            "final": [9.9, 9.9, 9.8, 9.8]
        },
        "Los Millonarios": {
            "preliminares": [9.3, 9.4, 9.5, 9.6],
            "cuartos": [9.6, 9.5, 9.7, 9.8],
            "semifinal": [9.7, 9.6, 9.7, 9.8]
        }
    },
    "coros": {
        "La Trinidad": {
            "preliminares": [9.0, 9.1, 9.2, 9.3],
            "cuartos": [9.3, 9.4, 9.5, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.8],
            "final": [9.7, 9.8, 9.9, 9.8]
        },
        "El Batallón Fletilla": {
            "preliminares": [8.8, 8.9, 9.0, 9.1],
            "cuartos": [9.0, 9.1, 9.2, 9.3],
            "semifinal": [9.2, 9.3, 9.4, 9.5]
        }
    },
    "cuartetos": {
        "Tres notas Musicales": {
            "preliminares": [9.2, 9.3, 9.1, 9.4],
            "cuartos": [9.4, 9.5, 9.3, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.6],
            "final": [9.7, 9.8, 9.6, 9.7]
        },
        "Ser o no Ser": {
            "preliminares": [8.7, 8.8, 8.9, 8.6],
            "cuartos": [8.9, 9.0, 8.8, 8.9]
        }
    }
}
def redondea_puntuacion(puntuacion):
    """Redondea una puntuación a dos decimales."""
    return round(puntuacion, 2)

def calcula_media_puntuaciones(grupos, *puntuaciones_extra, ag=None, fase=None):
    diccionario_resultado = {}

    for nombre_modalidad in grupos:
        for nombre_agrupacion in grupos[nombre_modalidad]:

            # si se pide una agrupacion saltamos la modalidad
            if ag is not None and nombre_agrupacion != ag:
                continue

            fases_de_la_agrupacion = grupos[nombre_modalidad][nombre_agrupacion]

            if ag is not None and fase is not None:
                # media de una sola fase 
                puntuaciones_redondeadas = list(
                    map(redondea_puntuacion, fases_de_la_agrupacion[fase])
                )
                extra_redondeadas = list(
                    map(redondea_puntuacion, puntuaciones_extra)
                )
                # lista nueva con todas las puntuaciones
                todas_las_puntuaciones = puntuaciones_redondeadas + extra_redondeadas
                # se calcula la media sumando todas las puntuaciónes entre la longitud de la lista
                media_calculada = sum(todas_las_puntuaciones) / len(todas_las_puntuaciones)
            else:
                # media general, media de las medias de cada fase
                suma_de_medias_de_fases = 0
                for nombre_fase in fases_de_la_agrupacion:
                    puntuaciones_redondeadas = list(
                        map(redondea_puntuacion, fases_de_la_agrupacion[nombre_fase])
                    )
                    media_de_la_fase = sum(puntuaciones_redondeadas) / len(puntuaciones_redondeadas)
                    suma_de_medias_de_fases = suma_de_medias_de_fases + media_de_la_fase
                media_calculada = suma_de_medias_de_fases / len(fases_de_la_agrupacion)

            # guardamos el resultado en el diccionario nuevo
            if nombre_modalidad not in diccionario_resultado:
                diccionario_resultado[nombre_modalidad] = {}
            diccionario_resultado[nombre_modalidad][nombre_agrupacion] = round(media_calculada, 2)

    return diccionario_resultado


# Pruebas 

print(calcula_media_puntuaciones(grupos))
print(calcula_media_puntuaciones(grupos, ag="Los Yesterday"))
print(calcula_media_puntuaciones(grupos, ag="Los Yesterday", fase="final"))
print(calcula_media_puntuaciones(grupos, 9.876, 9.944, ag="Los Yesterday", fase="final"))