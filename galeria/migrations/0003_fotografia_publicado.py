# Generated by Django 5.2 on 2025-05-20 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria_alter_fotografia_legenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
