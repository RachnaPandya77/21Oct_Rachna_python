from django.contrib import admin
from .models import Doctor

# Register your models here.
class doc_data(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','name','specialization','experience','address','mobile']

admin.site.register(Doctor,doc_data)
