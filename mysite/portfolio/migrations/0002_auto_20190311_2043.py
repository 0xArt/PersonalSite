# Generated by Django 2.1.7 on 2019-03-12 03:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalogProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tags', models.CharField(max_length=400)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_image')),
            ],
        ),
        migrations.CreateModel(
            name='DigitalProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tags', models.CharField(max_length=400)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_image')),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
