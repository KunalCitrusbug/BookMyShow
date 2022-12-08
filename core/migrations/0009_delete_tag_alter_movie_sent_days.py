# Generated by Django 4.1.3 on 2022-12-07 09:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_movie_tag_movie_sent_days"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.AlterField(
            model_name="movie",
            name="sent_days",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("Drama", "Drama"),
                    ("Comedy", "Comedy"),
                    ("Action", "Action"),
                    ("Animations", "Animations"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]