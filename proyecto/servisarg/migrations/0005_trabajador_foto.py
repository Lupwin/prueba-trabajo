# Generated by Django 4.2 on 2023-06-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servisarg", "0004_alter_trabajador_usuario"),
    ]

    operations = [
        migrations.AddField(
            model_name="trabajador",
            name="foto",
            field=models.ImageField(
                blank=True, null=True, upload_to="trabajador_photos/"
            ),
        ),
    ]
