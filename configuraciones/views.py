from django.shortcuts import render

# Create your views here.
def configurciones(request):
 return render(request, "configuraciones/config.html")
