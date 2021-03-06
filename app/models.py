from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from markdownx.models import MarkdownxField


class DiscordAdmin(models.Model):
    userid = models.CharField(max_length=18, unique=True, verbose_name='User ID')
    nick = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    dj_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Django User')

    def __str__(self):
        return self.nick


class BotCommandEntry(models.Model):
    name = models.CharField(max_length=30, unique=True)
    entry_lang = models.CharField(max_length=5, default='es', unique=True)
    aliases = models.CharField(max_length=100, default='', blank=True)
    owner_only = models.BooleanField(default=False)
    bot_owner_only = models.BooleanField(default=False)
    allows_pm = models.BooleanField(default=True, verbose_name='Allows PM')
    short_desc = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    usage = models.TextField(default='', blank=True)
    config_help = models.TextField(default='', blank=True)

    class Meta:
        verbose_name = 'Bot Command Entry'
        verbose_name_plural = 'Bot Command Entries'
        unique_together = (('name', 'entry_lang'),)


class CustomPage(models.Model):
    POST_TYPES = (
        ('P1', 'Normal'),
        ('P2', 'Hero')
    )

    author = models.ForeignKey(DiscordAdmin, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=64, default='')
    subtitle = models.CharField(max_length=256, default='', null=True, blank=True)
    description = MarkdownxField(default='', null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True, null=False)
    content = MarkdownxField()
    icon_url = models.URLField(verbose_name='Page icon URL', default='', null=True, blank=True)
    template = models.CharField(max_length=2, default='P1', choices=POST_TYPES)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Custom Page'

    def __str__(self):
        return self.title
