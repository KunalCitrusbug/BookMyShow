# Generated by Django 4.1.3 on 2022-12-07 08:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_movie_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Anime', 'Anime')], max_length=100, null=True),
        ),
    ]
