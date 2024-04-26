# Generated by Django 5.0.4 on 2024-04-25 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0003_remove_cliente_pais_origen_id_and_more'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.cliente', verbose_name='cliente')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.producto', verbose_name='producto')),
            ],
            options={
                'verbose_name': 'compra',
                'verbose_name_plural': 'compras',
            },
        ),
    ]
