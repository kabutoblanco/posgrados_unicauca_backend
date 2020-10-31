# Generated by Django 2.2.3 on 2020-10-31 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d_information_management_app', '0002_academictraining'),
        ('a_students_app', '0004_studentgroupinvestigation_studentprofessor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgroupinvestigation',
            options={'verbose_name': 'Mis grupos de investigacion', 'verbose_name_plural': 'Mi grupo de investigacion'},
        ),
        migrations.AlterModelOptions(
            name='studentprofessor',
            options={'verbose_name': 'Director/Coodirectores', 'verbose_name_plural': 'Directores/Coodirector'},
        ),
        migrations.RemoveField(
            model_name='studentgroupinvestigation',
            name='line_investigation',
        ),
        migrations.AddField(
            model_name='studentgroupinvestigation',
            name='investigation_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='d_information_management_app.InvestigationGroup', verbose_name='grupo de investigacion'),
            preserve_default=False,
        ),
    ]
