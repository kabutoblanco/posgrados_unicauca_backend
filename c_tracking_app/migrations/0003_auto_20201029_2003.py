# Generated by Django 2.2.3 on 2020-10-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_tracking_app', '0002_auto_20201029_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdirector',
            options={'verbose_name': 'Evaluación del director', 'verbose_name_plural': 'Evaluaciones de los directores'},
        ),
        migrations.RemoveField(
            model_name='testdirector',
            name='credits',
        ),
        migrations.AddField(
            model_name='testdirector',
            name='value',
            field=models.IntegerField(choices=[(1, 'FAVORABLE'), (2, 'NO_FAVORABLE')], default=1),
        ),
    ]
