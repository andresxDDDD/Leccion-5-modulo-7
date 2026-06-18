
from django.urls import path
from . import views


# el requests  llega desde el router aca y cada ruta gatilla un funcion 
urlpatterns = [
   
    path("lista/",views.lista_libros, name="lista_libros"),
]