# Generated by Django 3.2 on 2021-04-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='arquivo_video',
            field=models.FileField(default=1, max_length=254, upload_to='videoItem', verbose_name='Vídeo'),
            preserve_default=False,
        ),
    ]