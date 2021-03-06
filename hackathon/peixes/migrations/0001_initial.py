# Generated by Django 2.1.2 on 2018-10-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peixe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_especie', models.CharField(default='', max_length=64, verbose_name='Nome da Espécie de Peixe')),
                ('tempo_medio_crescimento', models.PositiveIntegerField(default=0, verbose_name='Tempo Médio de Crescimento')),
                ('tipo_racoes', models.CharField(choices=[('Farelada', 'Farelada'), ('Peletizada', 'Peletizada'), ('Extrusada', 'Extrusada')], default='Farelada', max_length=10, verbose_name='Tipo de Ração')),
                ('espaco_ocupacao', models.FloatField(default=0, verbose_name='Espaço de Ocupação em M²')),
                ('quantidade_racao', models.FloatField(default=0, verbose_name='Quantidade de Ração')),
                ('data_adicao', models.DateField(auto_now=True, verbose_name='Data de Adição')),
            ],
            options={
                'verbose_name': 'Peixe',
                'verbose_name_plural': 'Peixes',
            },
        ),
    ]
