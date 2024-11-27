# Generated by Django 5.0.9 on 2024-11-27 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacimiento', models.DateField()),
                ('experiencia', models.CharField(max_length=50)),
                ('certificacion', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('edad_maxima', models.IntegerField()),
                ('edad_minima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DirectorTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_division', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_programada', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=100)),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_inscripcion', models.CharField(max_length=50)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.categoria')),
                ('id_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.division')),
                ('id_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.directortecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Encuentro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('ubicacion_calle', models.CharField(max_length=200)),
                ('ubicacion_numero', models.CharField(max_length=20)),
                ('ubicacion_ciudad', models.CharField(max_length=100)),
                ('nombre_cancha', models.CharField(max_length=100)),
                ('id_arbitro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.arbitro')),
                ('id_fecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_ruedas', models.IntegerField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.categoria')),
                ('id_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.division')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('direccion_numero_calle', models.CharField(max_length=200)),
                ('url_foto', models.CharField(max_length=500)),
                ('contrasena', models.CharField(max_length=50)),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('mail', models.CharField(max_length=100)),
                ('num_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Gol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto_gol', models.IntegerField()),
                ('id_encuentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.encuentro')),
                ('num_socio_jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Rueda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('id_fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.fixture')),
            ],
        ),
        migrations.AddField(
            model_name='fecha',
            name='id_rueda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.rueda'),
        ),
        migrations.CreateModel(
            name='Sucede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_encuentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.encuentro')),
                ('id_gol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.gol')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('periodo_inicio', models.DateField()),
                ('periodo_fin', models.DateField()),
                ('estado_torneo', models.CharField(max_length=50)),
                ('inscripcion_fin', models.DateField()),
                ('inscripcion_inicio', models.DateField()),
                ('id_fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.fixture')),
                ('id_organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.organizador')),
            ],
        ),
        migrations.CreateModel(
            name='Involucra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(max_length=50)),
                ('id_encuentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.encuentro')),
                ('num_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.equipo')),
            ],
            options={
                'unique_together': {('id_encuentro', 'num_equipo')},
            },
        ),
        migrations.CreateModel(
            name='RealizaFalta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fue_expulsado', models.BooleanField()),
                ('cantidad_de_tarjetas', models.IntegerField()),
                ('id_encuentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.encuentro')),
                ('num_socio_jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.jugador')),
            ],
            options={
                'unique_together': {('id_encuentro', 'num_socio_jugador')},
            },
        ),
        migrations.CreateModel(
            name='TelefonoDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_director', models.CharField(max_length=20)),
                ('id_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.directortecnico')),
            ],
            options={
                'unique_together': {('telefono_director', 'id_tecnico')},
            },
        ),
        migrations.CreateModel(
            name='TelefonoJugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_jugador', models.CharField(max_length=20)),
                ('num_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.jugador')),
            ],
            options={
                'unique_together': {('telefono_jugador', 'num_socio')},
            },
        ),
        migrations.CreateModel(
            name='TelefonoOrganizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_organizador', models.CharField(max_length=20)),
                ('id_organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.organizador')),
            ],
            options={
                'unique_together': {('telefono_organizador', 'id_organizador')},
            },
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.equipo')),
                ('id_torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligaApp.torneo')),
            ],
            options={
                'unique_together': {('num_equipo', 'id_torneo')},
            },
        ),
    ]