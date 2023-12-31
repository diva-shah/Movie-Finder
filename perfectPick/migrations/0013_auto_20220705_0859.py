# Generated by Django 3.2.9 on 2022-07-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectPick', '0012_auto_20220705_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieID', models.IntegerField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='watchlist',
            field=models.ManyToManyField(related_name='watchlistItems', to='perfectPick.Integer'),
        ),
    ]
