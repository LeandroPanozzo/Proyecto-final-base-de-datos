from django.shortcuts import render, redirect
from .forms import JugadorForm
from .models import Jugador

def registrar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugador_listado')  # Redirige al listado de jugadores
    else:
        form = JugadorForm()
    return render(request, 'gestion/registrar_jugador.html', {'form': form})

def index(request):
    return render(request, 'gestion/index.html')  # Vista principal para /gestion/

# Vista para listar jugadores
def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'gestion/jugador_listado.html', {'jugadores': jugadores})

# Vista para editar un jugador
def editar_jugador(request, jugador_id):
    jugador = Jugador.objects.get(id=jugador_id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugador_listado')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'gestion/editar_jugador.html', {'form': form})


from .forms import EquipoForm
from .models import Equipo

def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo_listado')
    else:
        form = EquipoForm()
    return render(request, 'gestion/registrar_equipo.html', {'form': form})

# Vista para listar equipos
def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'gestion/equipo_listado.html', {'equipos': equipos})


from .forms import TorneoForm
from .models import Torneo

def registrar_torneo(request):
    if request.method == 'POST':
        form = TorneoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('torneo_listado')
    else:
        form = TorneoForm()
    return render(request, 'gestion/registrar_torneo.html', {'form': form})

# Vista para listar torneos
def listar_torneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'gestion/torneo_listado.html', {'torneos': torneos})


from .models import Division
from django.shortcuts import render, redirect

def registrar_division(request):
    if request.method == 'POST':
        nombre_division = request.POST.get('nombre_division')
        division = Division(nombre_division=nombre_division)
        division.save()
        return redirect('division_listado')
    return render(request, 'gestion/registrar_division.html')

# Vista para listar divisiones
def listar_divisiones(request):
    divisiones = Division.objects.all()
    return render(request, 'gestion/division_listado.html', {'divisiones': divisiones})


from .forms import CategoriaForm
from .models import Categoria

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_listado')
    else:
        form = CategoriaForm()
    return render(request, 'gestion/registrar_categoria.html', {'form': form})

# Vista para listar categorías
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestion/categoria_listado.html', {'categorias': categorias})


from .models import Arbitro
from django.shortcuts import render, redirect

def registrar_arbitro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        experiencia = request.POST.get('experiencia')
        certificacion = request.POST.get('certificacion')
        domicilio = request.POST.get('domicilio')
        nacimiento = request.POST.get('nacimiento')
        
        arbitro = Arbitro(nombre=nombre, experiencia=experiencia, certificacion=certificacion, 
                          domicilio=domicilio, nacimiento=nacimiento)
        arbitro.save()
        return redirect('arbitro_listado')
    
    return render(request, 'gestion/registrar_arbitro.html')

# Vista para listar árbitros
def listar_arbitros(request):
    arbitros = Arbitro.objects.all()
    return render(request, 'gestion/arbitro_listado.html', {'arbitros': arbitros})


from .models import Encuentro
from django.shortcuts import render, redirect

def registrar_encuentro(request):
    if request.method == 'POST':
        id_fecha = request.POST.get('id_fecha')
        estado = request.POST.get('estado')
        ubicacion_calle = request.POST.get('ubicacion_calle')
        ubicacion_numero = request.POST.get('ubicacion_numero')
        ubicacion_ciudad = request.POST.get('ubicacion_ciudad')
        nombre_cancha = request.POST.get('nombre_cancha')
        id_arbitro = request.POST.get('id_arbitro')
        
        encuentro = Encuentro(id_fecha=id_fecha, estado=estado, ubicacion_calle=ubicacion_calle,
                              ubicacion_numero=ubicacion_numero, ubicacion_ciudad=ubicacion_ciudad,
                              nombre_cancha=nombre_cancha, id_arbitro=id_arbitro)
        encuentro.save()
        return redirect('encuentro_listado')
    
    return render(request, 'gestion/registrar_encuentro.html')

# Vista para listar encuentros
def listar_encuentros(request):
    encuentros = Encuentro.objects.all()
    return render(request, 'gestion/encuentro_listado.html', {'encuentros': encuentros})
