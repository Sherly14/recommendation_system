# Generated by Django 4.0.3 on 2022-03-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_movie_song_name_song_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='movie_name',
            field=models.ManyToManyField(related_name='movie_name1', to='myapp.movie'),
        ),
    ]
