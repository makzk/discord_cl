# Generated by Django 2.1.2 on 2018-10-27 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20181027_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordadmin',
            name='dj_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Django User'),
        ),
    ]
