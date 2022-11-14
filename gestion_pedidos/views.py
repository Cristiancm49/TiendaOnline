from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestion_pedidos.forms import Formulario_contacto


# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["producto"]:

        #mensaje="Usted busco: %r" %request.GET["producto"]

        productos = request.GET["producto"]

        if len(productos)>20:
            mensaje = "Texto de busqueda demasiadfo largo"
        else:
            articulos= Articulos.objects.filter(nombre__icontains=productos)
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":productos})

    else:
        mensaje = "No introduciste un producto valido"
    return HttpResponse(mensaje)


def contacto(request):
    ## Esto se utiliza con los formularios creados manualmente.
   ## if request.method=="POST":
    ##    subject = request.POST['asunto']
    ##    mensaje = request.POST['mensaje'] + '' + request.POST['email']
    ##    email_from = settings.EMAIL_HOST_USER
    ##    recipient_list = ["ccortesm20001@gmail.com"]
    ##    send_mail(subject, mensaje, email_from, recipient_list)
    ##    return render(request, "index.html")
##  return render(request, "contacto.html")

## Lo siguente es el proceso con los formularios aotumaticos de API Forms
    if request.method == "POST":
        mi_formulario = Formulario_contacto(request.POST)
        if mi_formulario.is_valid():
            info_form = mi_formulario.cleaned_data
            send_mail(info_form['asunto'], info_form['mensaje'], info_form.get('email',''), 
            ['ccortesm20001@gmail.com'],)

            return render(request, "index.html")
    else:
        mi_formulario = Formulario_contacto()
    return render(request, "formulario_contacto.html", {"form": mi_formulario}) 