# Generated by Django 2.1.2 on 2018-10-29 01:50

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_custompage_icon_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompage',
            name='description',
            field=markdownx.models.MarkdownxField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='icon_url',
            field=models.URLField(default='', null=True, verbose_name='Page icon URL'),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='subtitle',
            field=models.CharField(default='', max_length=256, null=True),
        ),
    ]