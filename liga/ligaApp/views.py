from django.shortcuts import render, redirect
from .forms import JugadorForm
from .models import Jugador
from django.db import connection
from django.http import JsonResponse
from django.http import HttpResponse
import pyodbc
import uuid
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
import logging

# Configurar el logger
logger = logging.getLogger(__name__)



def generar_token(user_data):
    # Crear un token Refresh manualmente
    refresh = RefreshToken()

    # Obtener el access token
    access_token = refresh.access_token

    # Agregar el tipo de usuario y nombre de usuario al payload
    access_token['user_type'] = user_data['user_type']
    access_token['username'] = user_data['nombre_usuario']

    # Devolver el token como string
    return str(access_token)

# Función para verificar si el nombre de usuario y la contraseña son correctos en cualquiera de las tablas
def verificar_usuario_con_sql(username, password):
    # Consulta SQL para buscar el usuario en las tres tablas
    query = """
    SELECT TOP 1 'jugador' AS user_type, nombre_usuario AS nombre_usuario, contrasena AS password
    FROM Jugador
    WHERE nombre_usuario = %s
    UNION ALL
    SELECT TOP 1 'tecnico' AS user_type, nombre_usuario AS nombre_usuario, contrasena AS password
    FROM Director_tecnico
    WHERE nombre_usuario = %s
    UNION ALL
    SELECT TOP 1 'organizador' AS user_type, nombre_usuario AS nombre_usuario, contrasena AS password
    FROM Organizador
    WHERE nombre_usuario = %s
    """
    try:
        with connection.cursor() as cursor:
            # Pasar los parámetros necesarios
            cursor.execute(query, [username, username, username])
            result = cursor.fetchone()
            
        if result:
            # Log para ver el resultado de la consulta
            logger.debug(f"Resultado de la consulta para el usuario {username}: {result}")

            # Obtener la contraseña almacenada
            stored_password = result[2]  # Contraseña almacenada en la base de datos

            # Comparar la contraseña proporcionada con la almacenada
            if password == stored_password:
                # Si las contraseñas coinciden, devolver los datos
                return {
                    'user_type': result[0],
                    'nombre_usuario': result[1],
                    'password': result[2]
                }
            else:
                # Contraseña incorrecta
                logger.warning(f"Contraseña incorrecta para el usuario {username}")
                return None
        else:
            # Usuario no encontrado
            logger.warning(f"Usuario no encontrado: {username}")
            return None
    except Exception as e:
        # Manejar errores
        logger.error(f"Error al ejecutar la consulta: {e}")
        return None



# Vista para el login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_data = verificar_usuario_con_sql(username, password)

        if user_data:
            token = generar_token(user_data)

            # Store information in session
            request.session['token'] = token
            request.session['user_type'] = user_data['user_type']
            request.session['username'] = user_data['nombre_usuario']

            return JsonResponse({
                "token": token, 
                "user_type": user_data['user_type']
            })
        else:
            return JsonResponse({"error": "Usuario o contraseña incorrectos."}, status=400)

    return render(request, 'gestion/login.html')



def registrar_usuario(request, tabla):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si el nombre de usuario ya existe
        if verificar_existencia(username):
            return JsonResponse({"error": "El nombre de usuario ya existe"}, status=400)

        # Inserción en la tabla correspondiente (sin email)
        insert_query = f"""
        INSERT INTO {tabla} (nombre_usuario, contrasena)
        VALUES (%s, %s);
        """
        with connection.cursor() as cursor:
            cursor.execute(insert_query, [username, password])

        return JsonResponse({"message": "Registro exitoso"}, status=201)

    return render(request, f"register_{tabla}.html")


def register_jugador(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si el nombre de usuario ya existe en alguna tabla
        if verificar_existencia(username):
            return JsonResponse({"error": "El nombre de usuario ya existe en otra tabla."}, status=400)

        # Registrar el jugador (solo con nombre de usuario y contraseña)
        return registrar_usuario(request, "Jugador")

    return render(request, "gestion/register_jugador.html")

def register_organizador(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si el nombre de usuario ya existe en alguna tabla
        if verificar_existencia(username):
            return JsonResponse({"error": "El nombre de usuario ya existe en otra tabla."}, status=400)

        # Registrar el organizador (solo con nombre de usuario y contraseña)
        return registrar_usuario(request, "Organizador")

    return render(request, "gestion/register_organizador.html")

def register_director_tecnico(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si el nombre de usuario ya existe en alguna tabla
        if verificar_existencia(username):
            return JsonResponse({"error": "El nombre de usuario ya existe en otra tabla."}, status=400)

        # Registrar el director técnico (solo con nombre de usuario y contraseña)
        return registrar_usuario(request, "Director_tecnico")

    return render(request, "gestion/register_director_tecnico.html")

#Verifica existencia de un usuario con email y username especifico
def verificar_existencia(username):
    query = """
    SELECT 1
    FROM (
        SELECT nombre_usuario FROM Director_tecnico
        UNION ALL
        SELECT nombre_usuario FROM Jugador
        UNION ALL
        SELECT nombre_usuario FROM Organizador
    ) AS Combined
    WHERE nombre_usuario = %s;
    """
    with connection.cursor() as cursor:
        cursor.execute(query, [username])
        result = cursor.fetchone()
    return result is not None


def index(request):
    return render(request, 'gestion/index.html')  # Vista principal para /gestion/

from django.contrib.auth.decorators import login_required

@login_required
def editar_datos_usuario(request):
    user_type = request.user.user_type  # Determina el tipo de usuario

    if request.method == 'GET':
        usuario = None

        # Ejecuta consulta SQL para obtener los datos del usuario
        with connection.cursor() as cursor:
            if user_type == 'jugador':
                cursor.execute("SELECT * FROM gestion_jugador WHERE nombre_usuario = %s", [request.user.username])
                usuario = cursor.fetchone()
            elif user_type == 'tecnico':
                cursor.execute("SELECT * FROM gestion_director_tecnico WHERE nombre_usuario = %s", [request.user.username])
                usuario = cursor.fetchone()
            elif user_type == 'organizador':
                cursor.execute("SELECT * FROM gestion_organizador WHERE nombre_usuario = %s", [request.user.username])
                usuario = cursor.fetchone()
            else:
                return JsonResponse({"error": "Tipo de usuario desconocido"}, status=400)

        # Asegúrate de convertir el resultado a un diccionario si es necesario
        return render(request, 'gestion/editar_datos_usuario.html', {'usuario': usuario, 'user_type': user_type})

    elif request.method == 'POST':
        # Actualizar los datos del usuario según el tipo
        data = request.POST
        with connection.cursor() as cursor:
            if user_type == 'jugador':
                cursor.execute("""
                    UPDATE gestion_jugador
                    SET Nombre = %s, Apellido = %s, Telefono = %s
                    WHERE nombre_usuario = %s
                """, [data.get('Nombre'), data.get('Apellido'), data.get('Telefono'), request.user.username])
            elif user_type == 'tecnico':
                cursor.execute("""
                    UPDATE gestion_director_tecnico
                    SET Nombre = %s, Apellido = %s
                    WHERE nombre_usuario = %s
                """, [data.get('Nombre'), data.get('Apellido'), request.user.username])
            elif user_type == 'organizador':
                cursor.execute("""
                    UPDATE gestion_organizador
                    SET Nombre = %s, Apellido = %s, Telefono = %s
                    WHERE nombre_usuario = %s
                """, [data.get('Nombre'), data.get('Apellido'), data.get('Telefono'), request.user.username])
            else:
                return JsonResponse({"error": "Tipo de usuario desconocido"}, status=400)

        return JsonResponse({"message": "Datos actualizados correctamente"}, status=200)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@login_required
def perfil_usuario(request):
    # Check if token exists in session or headers
    token = request.session.get('token') or request.headers.get('Authorization')
    
    if not token:
        return JsonResponse({"error": "No autorizado"}, status=401)

    # Retrieve user information from session or token
    user_type = request.session.get('user_type')
    username = request.session.get('username')

    if not user_type or not username:
        return JsonResponse({"error": "Información de usuario no encontrada"}, status=401)

    # Prepare context with user information
    context = {
        'username': username,
        'user_type': user_type,
    }

    return render(request, 'gestion/perfil_usuario.html', context)

def home(request):
    return render(request, 'gestion/home.html')  # Asegúrate de que la ruta esté correcta
