from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista.html', {'libros': libros})