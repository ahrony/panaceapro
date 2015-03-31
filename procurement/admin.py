from django.contrib import admin
from .models import *


# Register your models here.
class RepairItemDetailInline(admin.TabularInline):
	model = RepairItemDetail
	extra = 2
	exclude = ("created_by","updated_by")
class AssetRepairModelAdmin(admin.ModelAdmin):
	inlines = [RepairItemDetailInline,]


admin.site.register(AssetRepair,AssetRepairModelAdmin)
