from django.contrib import admin

from .models import Country, Comment, WebUser

admin.site.register(Country)
admin.site.register(Comment)
admin.site.register(WebUser)