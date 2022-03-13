# Generated by Django 4.0.3 on 2022-03-12 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_singer_uuid_remove_song_singer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='singer_name',
            field=models.ManyToManyField(related_name='singer_name1', to='myapp.singer'),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=100)),
                ('song_name', models.ManyToManyField(related_name='song_name1', to='myapp.song')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]