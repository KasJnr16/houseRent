# Generated by Django 5.0.1 on 2024-01-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseInfo', '0002_alter_house_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image1',
            field=models.ImageField(null=True, upload_to='house_images'),
        ),
        migrations.AddField(
            model_name='house',
            name='image2',
            field=models.ImageField(null=True, upload_to='house_images'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(upload_to='house_images'),
        ),
    ]
