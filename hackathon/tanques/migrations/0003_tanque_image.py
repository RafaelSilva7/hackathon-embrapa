# Generated by Django 2.1.2 on 2018-10-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanques', '0002_auto_20181020_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanque',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tanques/images', verbose_name='Imagem'),
        ),
    ]
