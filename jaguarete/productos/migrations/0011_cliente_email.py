# Generated by Django 3.2.4 on 2021-06-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_canasta_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='rubenjguerra@yahoo.com', help_text='e-mail del cliente', max_length=100),
            preserve_default=False,
        ),
    ]
