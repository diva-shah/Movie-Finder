# Generated by Django 3.2.9 on 2022-07-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectPick', '0014_remove_integer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='liked',
            field=models.ManyToManyField(related_name='liked', to='perfectPick.Integer'),
        ),
    ]
