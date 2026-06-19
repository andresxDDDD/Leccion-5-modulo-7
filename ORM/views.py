from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista.html', {'libros': libros})


def libro_gabriel(request):

    # Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
    libro = Libro.objects.filter(autor="Gabriel García Márquez")
   

    # Recupera los libros que tienen más de 200 páginas.

    pagina = Libro.objects.filter(paginas__gt=200)

    #Aplica un filtro para mostrar solo libros disponibles.

    disponibilidad= Libro.objects.filter(disponible=True)


    return render(request,'consultas.html', {'libro':libro,'pagina':pagina,'dispo':disponibilidad})