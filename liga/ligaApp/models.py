from django.db import models

# Tabla Division
class Division(models.Model):
    nombre_division = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_division

# Tabla Categoria
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    edad_maxima = models.IntegerField()
    edad_minima = models.IntegerField()

    def __str__(self):
        return self.nombre_categoria

# Tabla Director Tecnico
class DirectorTecnico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla Equipo
class Equipo(models.Model):
    id_tecnico = models.ForeignKey(DirectorTecnico, on_delete=models.CASCADE)
    id_division = models.ForeignKey(Division, on_delete=models.CASCADE)
    estado_inscripcion = models.CharField(max_length=50)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Equipo {self.id_tecnico} - {self.id_categoria}"

# Tabla Jugador
class Jugador(models.Model):
    num_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    direccion_numero_calle = models.CharField(max_length=200)
    url_foto = models.CharField(max_length=500)
    contrasena = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla Telefono Director
class TelefonoDirector(models.Model):
    telefono_director = models.CharField(max_length=20)
    id_tecnico = models.ForeignKey(DirectorTecnico, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('telefono_director', 'id_tecnico')

# Tabla Telefono Jugador
class TelefonoJugador(models.Model):
    telefono_jugador = models.CharField(max_length=20)
    num_socio = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('telefono_jugador', 'num_socio')

# Tabla Organizador
class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla Telefono Organizador
class TelefonoOrganizador(models.Model):
    telefono_organizador = models.CharField(max_length=20)
    id_organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('telefono_organizador', 'id_organizador')

# Tabla Fixture
class Fixture(models.Model):
    id_division = models.ForeignKey(Division, on_delete=models.CASCADE)
    cant_ruedas = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

# Tabla Torneo
class Torneo(models.Model):
    id_organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    id_fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    estado_torneo = models.CharField(max_length=50)
    inscripcion_fin = models.DateField()
    inscripcion_inicio = models.DateField()

# Tabla Rueda
class Rueda(models.Model):
    id_fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    numero = models.IntegerField()

# Tabla Fecha
class Fecha(models.Model):
    id_rueda = models.ForeignKey(Rueda, on_delete=models.CASCADE)
    fecha_programada = models.DateField()

# Tabla Arbitro
class Arbitro(models.Model):
    nacimiento = models.DateField()
    experiencia = models.CharField(max_length=50)
    certificacion = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)

# Tabla Encuentro
class Encuentro(models.Model):
    id_fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    ubicacion_calle = models.CharField(max_length=200)
    ubicacion_numero = models.CharField(max_length=20)
    ubicacion_ciudad = models.CharField(max_length=100)
    nombre_cancha = models.CharField(max_length=100)
    id_arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)

# Tabla Gol
class Gol(models.Model):
    num_socio_jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    id_encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)
    minuto_gol = models.IntegerField()

# Tabla RealizaFalta
class RealizaFalta(models.Model):
    id_encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)
    num_socio_jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    fue_expulsado = models.BooleanField()
    cantidad_de_tarjetas = models.IntegerField()

    class Meta:
        unique_together = ('id_encuentro', 'num_socio_jugador')

# Tabla Sucede
class Sucede(models.Model):
    id_encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)
    id_gol = models.ForeignKey(Gol, on_delete=models.CASCADE)

# Tabla Participa
class Participa(models.Model):
    num_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('num_equipo', 'id_torneo')

# Tabla Involucra
class Involucra(models.Model):
    id_encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)
    num_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=50)

    class Meta:
        unique_together = ('id_encuentro', 'num_equipo')
