from django.contrib import admin
from .models import *


## New User Form Inline ##

class EmailCombinationInline(admin.StackedInline):
	model = EmailCombination
	extra = 3
	exclude = ("created_by","updated_by")

class NewUserModelAdmin(admin.ModelAdmin):
	inlines = [EmailCombinationInline,]

## Reference Model Inline ##
class IncomeSalarySlipInline(admin.TabularInline):
	model = IncomeSalarySlip
	extra = 6
	exclude = ("created_by","updated_by")

class PaySlipModelAdmin(admin.ModelAdmin):
	inlines = [IncomeSalarySlipInline,]

## Clearance Model Inline ##

class ReportingInline(admin.TabularInline):
	model = Reporting
	extra = 6
	exclude = ("created_by","updated_by")


class ClearanceModelAdmin(admin.ModelAdmin):
	inlines = [ReportingInline,]



admin.site.register(NewUser,NewUserModelAdmin)
admin.site.register(ReferenceCheck)
admin.site.register(ManPowerRequsition)
admin.site.register(NewHire)
admin.site.register(Disciplinary)
admin.site.register(TrainingBook)
admin.site.register(Enrollment)
admin.site.register(Clearance,ClearanceModelAdmin)
admin.site.register(PaySlip,PaySlipModelAdmin)