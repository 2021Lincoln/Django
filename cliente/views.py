from django.shortcuts import render

# Create your views here.
def fcliente(request):
    return render(request, "cad_cliente.html")