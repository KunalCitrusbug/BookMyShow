# Generated by Django 4.1.3 on 2022-11-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_movie_banner_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
