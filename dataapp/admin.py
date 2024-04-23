from django.contrib import admin
from django import forms
from . models import *

# Register your models here.

class mojoAdminForm(forms.ModelForm):
    list_display = ['Item_Code','Item_name']
    search_fields = ['Item_Code', 'Item_name']
    class Meta:
        model = mojo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        field_to_check = cleaned_data.get('Item_Code')

        # Check if the value already exists in the database
        if mojo.objects.filter(Item_Code=field_to_check).exists():
            raise forms.ValidationError("This value already exists.")

        return cleaned_data

class MojoAdmin(admin.ModelAdmin):
    form = mojoAdminForm
    list_display = ['Item_Code','Item_name']
    search_fields = ['Item_Code', 'Item_name']

admin.site.register(mojo, MojoAdmin )


# Qud30534