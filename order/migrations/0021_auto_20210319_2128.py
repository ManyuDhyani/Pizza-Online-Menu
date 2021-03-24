# Generated by Django 3.1.7 on 2021-03-19 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20210319_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prizesize',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.category'),
        ),
        migrations.AlterField(
            model_name='prizesize',
            name='prize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.prize'),
        ),
        migrations.AlterField(
            model_name='prizesize',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.size'),
        ),
    ]
