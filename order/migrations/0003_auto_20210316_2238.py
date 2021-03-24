# Generated by Django 3.1.7 on 2021-03-16 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_prize_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='pizza',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.prize'),
        ),
    ]