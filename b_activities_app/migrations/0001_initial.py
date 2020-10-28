# Generated by Django 2.2.3 on 2020-10-28 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=148)),
                ('receipt', models.FileField(upload_to='b_activities_app/archivos')),
                ('state', models.IntegerField(choices=[(1, 'REGISTRADO'), (2, 'EN_REVISION'), (3, 'REVISADA'), (4, 'ACEPTADA')], default=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('academic_year', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='ParticipationProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=40)),
                ('code_VRI', models.IntegerField()),
                ('convocation', models.CharField(max_length=40)),
                ('typo_convocation', models.CharField(max_length=100)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Participación en proyecto de investigación',
                'verbose_name_plural': 'Participaciónes en proyectos de investigación',
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ponencia en congreso / Simposio / Jornada',
                'verbose_name_plural': 'Ponencias en congresos / Simposios / Jornadas',
            },
        ),
        migrations.CreateModel(
            name='PresentationResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modality', models.CharField(max_length=40)),
                ('duration', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Exposición de resultados parciales de investigación',
                'verbose_name_plural': 'Exposiciónes de resultados parciales de investigación',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
            },
        ),
        migrations.CreateModel(
            name='ProjectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_hours', models.PositiveIntegerField()),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Curso / Direccion de proyectos / Revision de proyectos',
                'verbose_name_plural': 'Cursos / Direcciones de proyectos / Revisiones de proyectos',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('authors', models.CharField(max_length=80)),
                ('general_data', models.CharField(max_length=148)),
                ('editorial', models.CharField(max_length=100)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='ResearchStays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=20)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='b_activities_app.Activity')),
            ],
            options={
                'verbose_name': 'Estancia de investigación en otras instituciones',
                'verbose_name_plural': 'Estancias de investigación en otras instituciones',
            },
        ),
    ]
