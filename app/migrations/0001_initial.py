# Generated by Django 2.1.5 on 2019-02-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('field', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('course_description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
    ]
