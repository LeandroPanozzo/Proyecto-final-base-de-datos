from django import forms
from .models import Arbitro, Categoria, DirectorTecnico, Encuentro, Fecha, Fixture, Gol, Involucra, Jugador, Equipo, Organizador, Participa, RealizaFalta, Rueda, Sucede, TelefonoDirector, TelefonoJugador, TelefonoOrganizador, Torneo  # Importa los modelos necesarios

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'direccion_numero_calle', 'url_foto', 'contrasena', 'nombre_usuario', 'mail']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['id_tecnico', 'id_division', 'estado_inscripcion', 'id_categoria']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['id_organizador', 'id_fixture', 'nombre', 'periodo_inicio', 'periodo_fin', 'estado_torneo', 'inscripcion_fin', 'inscripcion_inicio']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'edad_maxima', 'edad_minima']

class DirectorTecnicoForm(forms.ModelForm):
    class Meta:
        model = DirectorTecnico
        fields = ['nombre', 'apellido', 'nombre_usuario', 'contrasena']

class TelefonoDirectorForm(forms.ModelForm):
    class Meta:
        model = TelefonoDirector
        fields = ['telefono_director', 'id_tecnico']

class TelefonoJugadorForm(forms.ModelForm):
    class Meta:
        model = TelefonoJugador
        fields = ['telefono_jugador', 'num_socio']

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'apellido', 'telefono', 'mail', 'nombre_usuario', 'contrasena']

class TelefonoOrganizadorForm(forms.ModelForm):
    class Meta:
        model = TelefonoOrganizador
        fields = ['telefono_organizador', 'id_organizador']

class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['id_division', 'cant_ruedas', 'id_categoria']

class RuedaForm(forms.ModelForm):
    class Meta:
        model = Rueda
        fields = ['id_fixture', 'numero']

class FechaForm(forms.ModelForm):
    class Meta:
        model = Fecha
        fields = ['id_rueda', 'fecha_programada']

class ArbitroForm(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ['nacimiento', 'experiencia', 'certificacion', 'domicilio', 'nombre']

class EncuentroForm(forms.ModelForm):
    class Meta:
        model = Encuentro
        fields = ['id_fecha', 'estado', 'ubicacion_calle', 'ubicacion_numero', 'ubicacion_ciudad', 'nombre_cancha', 'id_arbitro']

class GolForm(forms.ModelForm):
    class Meta:
        model = Gol
        fields = ['num_socio_jugador', 'id_encuentro', 'minuto_gol']

class RealizaFaltaForm(forms.ModelForm):
    class Meta:
        model = RealizaFalta
        fields = ['id_encuentro', 'num_socio_jugador', 'fue_expulsado', 'cantidad_de_tarjetas']

class SucedeForm(forms.ModelForm):
    class Meta:
        model = Sucede
        fields = ['id_encuentro', 'id_gol']

class ParticipaForm(forms.ModelForm):
    class Meta:
        model = Participa
        fields = ['num_equipo', 'id_torneo']

class InvolucraForm(forms.ModelForm):
    class Meta:
        model = Involucra
        fields = ['id_encuentro', 'num_equipo', 'resultado']
