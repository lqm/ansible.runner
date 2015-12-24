from django.contrib import admin
from web import models
# Register your models here.
class group_fuckid(admin.ModelAdmin):
    list_display = ('Use_by_group','unic_group',)
admin.site.register(models.group_fuckid)
