# Generated by Django 2.0.6 on 2018-09-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180831_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=400),
        ),
    ]