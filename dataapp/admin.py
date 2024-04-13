from django.contrib import admin
from . models import *

# Register your models here.
class MojoAdmin(admin.ModelAdmin):
    list_display = ['Item_Code','Item_name']
    search_fields = ['Item_Code', 'Item_name']

admin.site.register(mojo,MojoAdmin)