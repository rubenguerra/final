# Generated by Django 3.2.4 on 2021-06-28 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20210624_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='canasta',
            name='nombre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.producto'),
            preserve_default=False,
        ),
    ]
