# Generated by Django 4.1.3 on 2022-11-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('banner', models.ImageField(upload_to='')),
                ('tags', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
