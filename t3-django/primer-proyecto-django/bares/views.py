from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.utils.html import escape
# Create your views here.
BARES = [
    {"id": 1, "nombre": "Casa Felipe", "barrio": "La Viña",
     "especialidad": "tortillitas de camarones", "precio": 18, "fundado": "2015-06-23"},
    {"id": 2, "nombre": "El Faro", "barrio": "El Pópulo",
     "especialidad": "choco frito", "precio": 30, "fundado": "2018-03-20"},
    {"id": 3, "nombre": "Bar Cañailla", "barrio": "La Viña",
     "especialidad": "cañailla", "precio": 22, "fundado": "2025-03-27"}
]
def conteo_bares_barrio():
    conteo = {}
    for bar in BARES:
        conteo[bar["barrio"]] = conteo.get(bar["barrio"],0) + 1
    return conteo

def detalle(request: HttpResponse, pk: int):
    
    for bar in BARES:
        
        if bar["id"] == pk:
                
            return render(request, "bares/detalle.html", {"bar": bar})
    
    return HttpResponseNotFound("No hay ningún bar con ese identificador.")

def portada(request: HttpRequest):
    """ al principio los bares viajan escapados y con el safe"""
    conteo = conteo_bares_barrio()
    contexto = {"bares": BARES,
                "conteo": conteo}
    return render(request, "bares/portada.html",contexto)

def listado(request):
    """ Cuando no tiene el safe los caracteres no se escapan por lo cual es como si estuvieran con los caracteres tal cual los metes y el navegador los interpreta como etiquetas si fuera el caso, y cuando pones el safe los caracteres llegan escapados, por lo cual ya no contarían por ejemplo como etiquetas""" 
    contexto = {"bares": BARES}
    return render(request, "bares/listado.html", contexto)

def inspector(request : HttpRequest):
    """ aparece mi IP de localhost porque es desde donde estoy realizando la petición y el host es localhost:8000 porque es hacia donde estoy realizando la petición """
    return HttpResponse(
        
        f"method: {request.method}\n"
        
        f"path:   {request.path}\n"
        
        f"GET:    {dict(request.GET)}\n"
        
        f"REMOTE_ADDR: {request.META['REMOTE_ADDR']}\n"

        f"Host: {request.headers.get('Host','desconocido')}\n",
        
        content_type="text/plain; charset=utf-8",
    
    )

def buscar(request):
    
    valores: list[str]= request.GET.getlist("q")
    
    termino = valores[0].casefold() if valores else ""
    
    if termino == "":
        
        return HttpResponse(
            
            "Escribe un término de búsqueda: /bares/buscar/?q=camarones"
        
        )
    
    aviso = ""
    
    if len(valores) > 1:
        
        aviso = "<p>El parámetro q llegó repetido; solo se atiende al primero.</p>"
    
    return HttpResponse(f"{aviso}<p>Buscando «{escape(termino)}»...</p>")

def plato(request: HttpRequest, pk: int):
    """Solo recibe un único argumento que es el id, no puede recibir más, y plato/ aporta solo la dirección para que se ejecute la vista."""
    for bar in BARES:
        
        if bar["id"] == pk:
                
            return HttpResponse(
                    
            f"<h1>{bar['nombre']}</h1><p>Barrio: {bar['barrio']}</p>"
            f"<p> El plato estrella del bar {bar['id']} es : {bar['especialidad']}"
            )
    
    return HttpResponseNotFound("No hay ningún bar con ese identificador.")