from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.



def cliente_agregar(request):
    if request.method=="GET":
        form = ClienteForm()
    
        return render(request,'cliente/agregar.html',{'form':form})

    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cliente/home.html')
    

    