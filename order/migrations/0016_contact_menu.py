# Generated by Django 3.1.7 on 2021-03-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_pizza_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='menu',
            field=models.FileField(null=True, upload_to='menu'),
        ),
    ]
