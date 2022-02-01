# Generated by Django 3.2 on 2021-04-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='imagem',
            name='arquivo_imagem',
            field=models.ImageField(default=1, upload_to='imagemItem', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
