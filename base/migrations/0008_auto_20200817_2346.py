# Generated by Django 3.1 on 2020-08-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200817_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_headline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
