# Generated by Django 2.2.3 on 2020-10-30 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d_information_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='d_information_management_app.Institution')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='d_information_management_app.Professor')),
            ],
            options={
                'verbose_name': 'Formacion Academica',
                'verbose_name_plural': 'Formaciones Academicas',
            },
        ),
    ]
