# Generated by Django 2.0.4 on 2018-04-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180423_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='botcommandentry',
            name='short_desc',
            field=models.TextField(blank=True, default=''),
        ),
    ]
