# Generated by Django 2.0.6 on 2018-07-13 23:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
