from django.db import models

# Create your models here.
class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey("auth.User", related_name="+",blank=True,null=True)
	updated_by = models.ForeignKey("auth.User", related_name="+",blank=True,null=True)

	class Meta:
		abstract = True



		