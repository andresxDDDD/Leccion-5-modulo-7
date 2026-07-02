
from django.urls import path
from . import views


# el requests  llega desde el router aca y cada ruta gatilla un funcion 
urlpatterns = [


    path('', views.index, name='index'),
    path('recuperacion/', views.vista_recuperacion, name='recuperacion'),
    path('filtros/', views.vista_filtros, name='filtros_exclusiones'),
    path('sql/', views.vista_sql, name='consultas_sql'),
    path('anotaciones/', views.vista_anotaciones, name='campos_anotaciones'),
]
