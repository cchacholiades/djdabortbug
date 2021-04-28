from django.contrib import admin
from .models import TestModel

class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_id',)

admin.site.register(TestModel, TestModelAdmin)