# Generated by Django 3.1.7 on 2021-03-16 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210316_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='price',
            new_name='prize',
        ),
    ]
