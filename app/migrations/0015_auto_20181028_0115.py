# Generated by Django 2.1.2 on 2018-10-28 04:15

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20181027_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompage',
            name='description',
            field=markdownx.models.MarkdownxField(default=''),
        ),
        migrations.AddField(
            model_name='custompage',
            name='subtitle',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='custompage',
            name='template',
            field=models.CharField(choices=[('P1', 'Normal'), ('P2', 'Hero')], default='P1', max_length=2),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]