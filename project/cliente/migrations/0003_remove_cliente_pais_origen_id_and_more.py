# Generated by Django 5.0.4 on 2024-04-25 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_producto_cliente_producto_adquirido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='pais_origen_id',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='producto_adquirido',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
