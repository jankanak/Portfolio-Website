# Generated by Django 3.1 on 2020-08-17 18:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200817_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_headline',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
