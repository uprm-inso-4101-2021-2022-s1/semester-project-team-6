# Generated by Django 3.2.8 on 2021-10-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='embed',
            field=models.TextField(),
        ),
    ]
