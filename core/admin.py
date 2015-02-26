from django.contrib import admin
from core.models import TestItem

# Register your models here.

class TestItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestItem, TestItemAdmin)

