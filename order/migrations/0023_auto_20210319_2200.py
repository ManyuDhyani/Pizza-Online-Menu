# Generated by Django 3.1.7 on 2021-03-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20210319_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='thumbnail',
            field=models.ImageField(default='images/gallery-img1.jpg', upload_to='images/pizza'),
        ),
    ]