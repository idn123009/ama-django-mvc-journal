from django.contrib import admin

from .models import Entry,Mood

# Register your models here.
admin.site.register(Entry)
admin.site.register(Mood)