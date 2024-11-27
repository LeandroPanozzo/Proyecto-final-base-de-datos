from django.urls import path
from . import views  # Asegúrate de importar las vistas que hemos creado
#urls.py de ligaApp
app_name = 'gestion'  # Aquí defines el espacio de nombres
urlpatterns = [
    # Rutas para Jugadores
    path('', views.index, name='gestion_index'),
    path('registrar_jugador/', views.registrar_jugador, name='registrar_jugador'),
    path('jugadores/', views.listar_jugadores, name='jugador_listado'),
    path('editar_jugador/<int:jugador_id>/', views.editar_jugador, name='editar_jugador'),

    # Rutas para Equipos
    path('registrar_equipo/', views.registrar_equipo, name='registrar_equipo'),
    path('equipos/', views.listar_equipos, name='equipo_listado'),

    # Rutas para Torneos
    path('registrar_torneo/', views.registrar_torneo, name='registrar_torneo'),
    path('torneos/', views.listar_torneos, name='torneo_listado'),

    # Rutas para Divisiones
    path('registrar_division/', views.registrar_division, name='registrar_division'),
    path('divisiones/', views.listar_divisiones, name='division_listado'),

    # Rutas para Categorías
    path('registrar_categoria/', views.registrar_categoria, name='registrar_categoria'),
    path('categorias/', views.listar_categorias, name='categoria_listado'),

    # Rutas para Árbitros
    path('registrar_arbitro/', views.registrar_arbitro, name='registrar_arbitro'),
    path('arbitros/', views.listar_arbitros, name='arbitro_listado'),

    # Rutas para Encuentros
    path('registrar_encuentro/', views.registrar_encuentro, name='registrar_encuentro'),
    path('encuentros/', views.listar_encuentros, name='encuentro_listado'),
]
