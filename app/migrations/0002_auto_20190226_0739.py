# Generated by Django 2.1.5 on 2019-02-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(height_field=100, upload_to='photo', width_field=100),
        ),
    ]
