# Generated by Django 3.2.9 on 2021-11-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
