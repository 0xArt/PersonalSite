# Generated by Django 2.0.6 on 2018-07-10 04:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
