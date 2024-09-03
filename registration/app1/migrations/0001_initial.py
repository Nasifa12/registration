# Generated by Django 4.1.3 on 2024-09-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_tittle', models.CharField(max_length=250)),
                ('poster', models.ImageField(upload_to='gallery')),
                ('description', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
                ('actors', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
            ],
        ),
    ]