# Generated by Django 4.2.2 on 2023-06-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
