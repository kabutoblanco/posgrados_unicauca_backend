# Generated by Django 2.2.3 on 2020-10-28 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoDirectorControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_period', models.CharField(max_length=20)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Control de codirector',
                'verbose_name_plural': 'Controles de codirector',
            },
        ),
        migrations.CreateModel(
            name='DirectorControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_period', models.CharField(max_length=20)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Control de director',
                'verbose_name_plural': 'Controles de director',
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetive_general', models.CharField(max_length=148)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Objetivo general',
                'verbose_name_plural': 'Objetivos generales',
            },
        ),
        migrations.CreateModel(
            name='Objetive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provisional_title', models.CharField(max_length=40)),
                ('objetive_topic', models.CharField(max_length=80)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Specific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetive_specific', models.CharField(max_length=148)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('objetive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_projects_app.Objetive')),
            ],
            options={
                'verbose_name': 'Objetivo especifico',
                'verbose_name_plural': 'Objetivos especificos',
            },
        ),
    ]
