# Generated by Django 2.2.1 on 2019-05-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0006_albums_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='album_logo',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
