from django.contrib import admin

from .models import *

# Register your models here.


class PresentEmployeeNameInline(admin.StackedInline):
	model = PresentEmployeeName
	extra = 10
	exclude = ("created_by", "updated_by")

class RoomBookModelAdmin(admin.ModelAdmin):
	inlines = [PresentEmployeeNameInline,]

admin.site.register(RoomBook,RoomBookModelAdmin)

