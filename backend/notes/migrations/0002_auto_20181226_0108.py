# Generated by Django 2.1.3 on 2018-12-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_squashed_0006_auto_20181223_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
