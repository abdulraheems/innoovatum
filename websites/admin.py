from django.contrib import admin
from .models import Website

# Register your models here.
admin.site.register(Website)

class WebsiteAdmin(admin.ModelAdmin):
    list_display  = ('title', 'link','content','logo')