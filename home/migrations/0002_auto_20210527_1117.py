# Generated by Django 3.2 on 2021-05-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='number',
            field=models.IntegerField(),
        ),
    ]
