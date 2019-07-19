from django.contrib import admin

from .models import ppo

class ppoAdmin(admin.ModelAdmin):
	list_display = ('id',)
	list_display_links = ('id',)
admin.site.register(ppo,ppoAdmin)
