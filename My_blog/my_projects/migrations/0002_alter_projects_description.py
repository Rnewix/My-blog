# Generated by Django 4.1 on 2022-09-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
