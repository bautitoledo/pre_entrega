# Generated by Django 4.1.3 on 2022-12-18 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFrailoni', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombrecliente',
            new_name='nombre',
        ),
    ]
