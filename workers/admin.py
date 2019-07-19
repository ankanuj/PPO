from django.contrib import admin
from .models import Worker

class WrokerAdmin(admin.ModelAdmin):
	list_display = ('id','first_name','email','phone')
	list_display_links = ('id','first_name')
	list_filter = ('first_name',)
	search_fields = ('first_name','last_name','email','phone')
	list_per_page = 25
admin.site.register(Worker,WrokerAdmin)
