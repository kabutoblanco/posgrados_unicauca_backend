# Generated by Django 2.2.3 on 2020-10-31 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_tracking_app', '0005_auto_20201030_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityprofessor',
            name='rol',
            field=models.IntegerField(choices=[(1, 'DIRECTOR'), (2, 'COODIRECTOR'), (3, 'COORDINADOR')], default=1, verbose_name='rol'),
        ),
    ]
