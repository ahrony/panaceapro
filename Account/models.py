from django.db import models

from base.models import BaseModel


## Contra Voucher ##

class ContraVoucher(BaseModel):
	voucher_no = models.CharField(max_length=128)
	date = models.DateField()
	paid_amount = models.TextField(max_length=1000,verbose_name="Being the amount paid for")
	amount_in_words = models.TextField(max_length=1000,verbose_name="Amount in words")
	prepared_by = models.CharField(max_length=128)
	chief_officer = models.CharField(max_length=128,verbose_name="Chief Executive Officer")
	certified_by = models.CharField(max_length=128,verbose_name="Certified/Accounts")

	## contra Voucher Details ##
class ContraDetail(BaseModel):
	parent_model = models.ForeignKey("Account.ContraVoucher",null=True)
	account_head = models.CharField(max_length=128,verbose_name="Head of Account")
	ledger_info = models.IntegerField(max_length=128,verbose_name="Ledger Folio")
	debit_info = models.IntegerField(max_length=128,verbose_name="DEBIT")
	credit_info = models.IntegerField(max_length=128,verbose_name="CREDIT")


# # Ledger Voucher Model ## 
class JournalVoucher(BaseModel):
	voucher_no = models.CharField(max_length=128)
	date = models.DateField()
	paid_amount = models.TextField(max_length=1000,verbose_name="Being the amount paid for")
	amount_in_words = models.TextField(max_length=1000,verbose_name="Amount in words")
	prepared_by = models.CharField(max_length=128)
	chief_officer = models.CharField(max_length=128,verbose_name="Chief Executive Officer")
	certified_by = models.CharField(max_length=128,verbose_name="Certified/Accounts")

	## ledger Voucher Details ##
class JournalDetail(BaseModel):
	parent_model = models.ForeignKey("Account.JournalVoucher",null=True)
	account_head = models.CharField(max_length=128,verbose_name="Head of Account")
	ledger_info = models.IntegerField(max_length=128,verbose_name="Ledger Folio")
	debit_info = models.IntegerField(max_length=128,verbose_name="DEBIT")
	credit_info = models.IntegerField(max_length=128,verbose_name="CREDIT")

# # Credit Voucher Model ## 
class CreditVoucher(BaseModel):
	voucher_no = models.CharField(max_length=128)
	date = models.DateField()
	paid_amount = models.TextField(max_length=1000,verbose_name="Being the amount paid for")
	amount_in_words = models.TextField(max_length=1000,verbose_name="Amount in words")
	prepared_by = models.CharField(max_length=128)
	chief_officer = models.CharField(max_length=128,verbose_name="Chief Executive Officer")
	certified_by = models.CharField(max_length=128,verbose_name="Certified/Accounts")

	## Credit Voucher Details ##
class CreditDetail(BaseModel):
	parent_model = models.ForeignKey("Account.CreditVoucher",null=True)
	account_head = models.CharField(max_length=128,verbose_name="Head of Account")
	ledger_info = models.IntegerField(max_length=128,verbose_name="Ledger Folio")
	debit_info = models.IntegerField(max_length=128,verbose_name="DEBIT")
	credit_info = models.IntegerField(max_length=128,verbose_name="CREDIT")

# # Debit Voucher Model ## 
class DebitVoucher(BaseModel):
	voucher_no = models.CharField(max_length=128)
	date = models.DateField()
	paid_amount = models.TextField(max_length=1000,verbose_name="Being the amount paid for")
	amount_in_words = models.TextField(max_length=1000,verbose_name="Amount in words")
	prepared_by = models.CharField(max_length=128)
	chief_officer = models.CharField(max_length=128,verbose_name="Chief Executive Officer")
	certified_by = models.CharField(max_length=128,verbose_name="Certified/Accounts")

	## Debit Voucher Details ##
class DebitDetail(BaseModel):
	parent_model = models.ForeignKey("Account.DebitVoucher",null=True)
	account_head = models.CharField(max_length=128,verbose_name="Head of Account")
	ledger_info = models.IntegerField(max_length=128,verbose_name="Ledger Folio")
	debit_info = models.IntegerField(max_length=128,verbose_name="DEBIT")
	credit_info = models.IntegerField(max_length=128,verbose_name="CREDIT")





