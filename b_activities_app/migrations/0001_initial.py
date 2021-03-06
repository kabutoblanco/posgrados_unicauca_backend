# Generated by Django 2.2.3 on 2020-10-29 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_students_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('description', models.CharField(max_length=148)),
                ('receipt', models.FileField(upload_to='b_activities_app/archivos')),
                ('state', models.IntegerField(choices=[(1, 'REGISTRADO'), (2, 'EN_REVISION'), (3, 'REVISADA'), (4, 'ACEPTADA')], default=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('academic_year', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_students_app.Student')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('place', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Ponencia en congreso / Simposio / Jornada',
                'verbose_name_plural': 'Ponencias en congresos / Simposios / Jornadas',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='ParticipationProjects',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('place', models.CharField(max_length=40)),
                ('code_VRI', models.IntegerField()),
                ('convocation', models.CharField(max_length=40)),
                ('type_convocation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Participación en proyecto de investigación',
                'verbose_name_plural': 'Participaciónes en proyectos de investigación',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='PresentationResults',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('modality', models.CharField(max_length=40)),
                ('duration_hours', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Exposición de resultados parciales de investigación',
                'verbose_name_plural': 'Exposiciónes de resultados parciales de investigación',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='ProjectCourse',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('assigned_hours', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Curso / Direccion de proyectos / Revision de proyectos',
                'verbose_name_plural': 'Cursos / Direcciones de proyectos / Revisiones de proyectos',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('type_publication', models.CharField(max_length=20)),
                ('authors', models.CharField(max_length=80)),
                ('general_data', models.CharField(max_length=148)),
                ('editorial', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='ResearchStays',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.Activity')),
                ('purpose', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Estancia de investigación en otras instituciones',
                'verbose_name_plural': 'Estancias de investigación en otras instituciones',
            },
            bases=('b_activities_app.activity',),
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='b_activities_app.Activity')),
            ],
            options={
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
            },
        ),
    ]
