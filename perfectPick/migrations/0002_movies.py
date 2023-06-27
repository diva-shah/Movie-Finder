# Generated by Django 3.2.9 on 2022-07-04 08:54

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectPick', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField()),
                ('cast', django_mysql.models.ListTextField(models.CharField(max_length=100), size=None)),
                ('genres', django_mysql.models.ListTextField(models.CharField(max_length=100), size=None)),
                ('title', models.CharField(max_length=100)),
                ('streaming', django_mysql.models.ListTextField(models.CharField(max_length=100), size=None)),
            ],
        ),
    ]