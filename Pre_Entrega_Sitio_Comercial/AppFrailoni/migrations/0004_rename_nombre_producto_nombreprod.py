# Generated by Django 4.1.3 on 2022-12-19 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFrailoni', '0003_remove_producto_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='nombreprod',
        ),
    ]
