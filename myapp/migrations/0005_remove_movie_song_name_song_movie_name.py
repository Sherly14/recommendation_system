# Generated by Django 4.0.3 on 2022-03-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_song_singer_name_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='song_name',
        ),
        migrations.AddField(
            model_name='song',
            name='movie_name',
            field=models.ManyToManyField(related_name='movie_name1', to='myapp.singer'),
        ),
    ]