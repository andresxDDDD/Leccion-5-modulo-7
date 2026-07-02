from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Libro

def index(request):
    
    return render(request, 'index.html')

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista.html', {'libros': libros})




# 1. Vista principal que ya creamos
def index(request):
    return render(request, 'index.html')

# 2. Vista para Recuperación de registros
from django.shortcuts import render
from .models import Libro  # Asegúrate de importar tu modelo Libro

def vista_recuperacion(request):

    libros = Libro.objects.all()

    # 1. Libros de Gabriel García Márquez
    libro = Libro.objects.filter(autor="Gabriel García Márquez")

    # 2. Libros con más de 200 páginas
    pagina = Libro.objects.filter(paginas__gt=200)

    

    # Enviamos todo al template
    return render(request, 'recuperacion.html', {
        'libro': libro,
        'pagina': pagina,
        'libros': libros,
    })
# 3. Vista para Filtros y exclusiones
def vista_filtros(request):

    # 3. Aplica un filtro para mostrar solo libros disponibles
   # disponibilidad = Libro.objects.filter(disponible=True)
    return render(request, 'filtros.html')

# 4. Vista para Consultas personalizadas con SQL
def vista_sql(request):
    return render(request, 'sql.html')

# 5. Vista para Campos específicos y anotaciones
def vista_anotaciones(request):
    return render(request, 'anotaciones.html')