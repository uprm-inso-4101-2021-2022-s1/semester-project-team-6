# Generated by Django 3.2.8 on 2021-10-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_code', models.CharField(max_length=10)),
                ('building_name', models.CharField(max_length=60)),
                ('embed', models.CharField(max_length=500)),
            ],
        ),
    ]