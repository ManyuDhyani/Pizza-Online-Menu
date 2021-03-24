# Generated by Django 3.1.7 on 2021-03-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('mobile1', models.CharField(max_length=50)),
                ('mobile2', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.CharField(max_length=30)),
                ('day', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]