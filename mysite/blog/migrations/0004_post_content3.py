# Generated by Django 2.0.6 on 2018-07-13 23:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content3',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
