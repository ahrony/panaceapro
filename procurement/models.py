from django.db import models

from base.models import BaseModel

## Asset Repaire & Maintenance Model ##

class AssetRepair(BaseModel):
	date = models.DateField()
	name = models.CharField(max_length=128)
	department = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	repair_complete_date = models.CharField(max_length=128,
											verbose_name="Recommended Repair Completion Date")
	manager = models.CharField(max_length=128,verbose_name="Manager/Team Leader")
	procure_manager = models.CharField(max_length=128,verbose_name="Manager procurement Department")
	chief_officer = models.CharField(max_length=128,verbose_name="Chief Executive Officer")

	## repaire item description under AssetRepair Model ##

class RepairItemDetail(BaseModel):
	parent_model = models.ForeignKey("procurement.AssetRepair")
	serial_no = models.IntegerField(max_length=30)
	item_name = models.CharField(max_length=128,verbose_name="Name of equipment in need of repair")
	detail = models.TextField(max_length=500,
							verbose_name="Details description of malfunction in need of repair")




