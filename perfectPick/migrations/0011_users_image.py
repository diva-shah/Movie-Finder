# Generated by Django 3.2.9 on 2022-07-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectPick', '0010_auto_20220705_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ManyToManyField(related_name='image', to='perfectPick.Integer'),
        ),
    ]
