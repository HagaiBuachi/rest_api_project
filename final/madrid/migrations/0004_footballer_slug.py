# Generated by Django 3.2.8 on 2021-10-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrid', '0003_alter_footballer_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballer',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
