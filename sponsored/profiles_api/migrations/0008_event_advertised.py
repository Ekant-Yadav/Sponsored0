# Generated by Django 3.1.5 on 2021-02-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0007_sponsoredevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='advertised',
            field=models.BooleanField(default=False),
        ),
    ]