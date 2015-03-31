from django.db import models

from base.models import BaseModel



## Conferenece Booking Form ##

class RoomBook(BaseModel):
	name = models.CharField(max_length=128,verbose_name="Conference Room Booked By")
	department = models.CharField(max_length=128)
	reason = models.CharField(max_length=128)
	date = models.DateField()
	period = models.CharField(max_length=128)
	number_of_employee = models.IntegerField(max_length=128,
											verbose_name="Number of Member(s) to be Present")


	## Present Employee list in Conference ##

class PresentEmployeeName(BaseModel):
	parent_model = models.ForeignKey("Adminmodel.RoomBook")
	name = models.CharField(max_length=128,verbose_name="Name")