# Generated by Django 2.2.3 on 2020-10-29 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_date', models.DateField()),
                ('period_academic', models.CharField(max_length=12)),
                ('percentage_discount', models.FloatField(default=0.0)),
                ('observation', models.CharField(max_length=148)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Convenio',
                'verbose_name_plural': 'Convenios',
            },
        ),
        migrations.CreateModel(
            name='Enrrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField()),
                ('enrrollment_date', models.DateField()),
                ('state', models.IntegerField(choices=[(1, 'GRADUADO'), (2, 'BALANCEADO'), (3, 'RETIRADO')])),
                ('period', models.CharField(max_length=24)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('announcement', models.DateField()),
                ('description', models.CharField(max_length=48)),
                ('num_resolution', models.CharField(max_length=48)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Beca',
                'verbose_name_plural': 'Becas',
            },
        ),
        migrations.CreateModel(
            name='GrantAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Beca/Convenio',
                'verbose_name_plural': 'Becas/Convenios',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=148)),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dedication', models.IntegerField(choices=[(1, 'COMPLETO'), (2, 'PARCIAL')], default=1)),
                ('date_record', models.DateTimeField()),
                ('date_update', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_students_app.Program')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
