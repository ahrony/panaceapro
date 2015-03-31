from django.contrib import admin
from .models import *


# Register your models here.

class ContraDetailInline(admin.TabularInline):
	model = ContraDetail
	extra = 4
	exclude = ("created_by","updated_by")
class ContraVoucherModelAdmin(admin.ModelAdmin):
	inlines = [ContraDetailInline,]

class JournalDetailInline(admin.TabularInline):
	model = JournalDetail
	extra = 4
	exclude = ("created_by","updated_by")
class JournalVoucherModelAdmin(admin.ModelAdmin):
	inlines = [JournalDetailInline,]

class CreditDetailInline(admin.TabularInline):
	model = CreditDetail
	extra = 4
	exclude = ("created_by","updated_by")
class CreditModelAdmin(admin.ModelAdmin):
	inlines = [CreditDetailInline,]

class DebitDetailInline(admin.TabularInline):
	model = DebitDetail
	extra = 4
	exclude = ("created_by","updated_by")
class DebitModelAdmin(admin.ModelAdmin):
	inlines = [DebitDetailInline,]



admin.site.register(ContraVoucher,ContraVoucherModelAdmin)
admin.site.register(JournalVoucher,JournalVoucherModelAdmin)
admin.site.register(CreditVoucher,CreditModelAdmin)
admin.site.register(DebitVoucher,DebitModelAdmin)
