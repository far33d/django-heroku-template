from django.contrib import admin
from core.models import TestItem, PurchaseRecord

# Register your models here.

class TestItemAdmin(admin.ModelAdmin):
    pass
class PurchaseRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestItem, TestItemAdmin)
admin.site.register(PurchaseRecord, PurchaseRecordAdmin)

