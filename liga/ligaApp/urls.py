from django.urls import path
from . import views  # Asegúrate de importar las vistas que hemos creado
from .views import perfil_usuario

#urls.py de ligaApp
app_name = 'gestion'  # Aquí defines el espacio de nombres
urlpatterns = [
    
    path("register/jugador/", views.register_jugador, name="register_jugador"),
    path("register/organizador/", views.register_organizador, name="register_organizador"),
    path("register/director_tecnico/", views.register_director_tecnico, name="register_director_tecnico"),
    path("login/", views.login, name="login"),
    # Rutas para Jugadores
    path('', views.index, name='gestion_index'),
    path('editar_datos/', views.editar_datos_usuario, name='editar_datos_usuario'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('home/', views.home, name='home'),

]
