# Generated by Django 4.1.3 on 2022-11-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
