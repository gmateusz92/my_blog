from django.contrib import admin
from .models import Topics, Comment, Calculator

admin.site.register(Topics)
admin.site.register(Comment)
admin.site.register(Calculator)