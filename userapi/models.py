from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.html import format_html
# create your models here.

class UserDetails(models.Model):
    login = models.CharField(max_length=30)
    avatar_url = models.URLField(null=True)
    repos_url = models.URLField(null=True)
    type = models.CharField(max_length=30)
    site_admin = models.BooleanField
    name = models.CharField(max_length=30,null=True)
    company = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    def admin_img(self):
        if self.avatar_url:
            return format_html('<img src="%s" height="75" />' %(self.avatar_url))
    admin_img.short_description = 'Profile'
    admin_img.allow_tags = 'True'