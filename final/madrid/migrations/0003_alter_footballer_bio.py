# Generated by Django 3.2.8 on 2021-10-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrid', '0002_rename_footballers_footballer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballer',
            name='bio',
            field=models.TextField(max_length=1000),
        ),
    ]
