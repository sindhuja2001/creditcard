from django.db import models

# Create your models here.
# class loginTable(models.Model):
#     id = models.IntegerField(primary_key=True)
#     emailId =  models.CharField(max_length=250, blank=False, null=False)
#     mailPassword = models.CharField(max_length=250, blank=False, null=False)

#     class Meta:
#         db_table = 'LOGIN'
    
class Userlogin(models.Model):
    id = models.IntegerField(primary_key=True)
    email=  models.CharField(max_length=250, blank=False, null=False)
    mailPassword = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        db_table = 'new_table'

class ManualInput(models.Model):
    id = models.IntegerField(primary_key=True)
    Time = models.FloatField(max_length=250, blank=False, null=False)
    V1 = models.FloatField(max_length=250, blank=False, null=False)
    V2 = models.FloatField(max_length=250, blank=False, null=False)
    V3 = models.FloatField(max_length=250, blank=False, null=False)
    V4 = models.FloatField(max_length=250, blank=False, null=False)
    V5 = models.FloatField(max_length=250, blank=False, null=False)
    V6 = models.FloatField(max_length=250, blank=False, null=False)
    V7 = models.FloatField(max_length=250, blank=False, null=False)
    V8 = models.FloatField(max_length=250, blank=False, null=False)
    V9 = models.FloatField(max_length=250, blank=False, null=False)
    V10 = models.FloatField(max_length=250, blank=False, null=False)
    V11 = models.FloatField(max_length=250, blank=False, null=False)
    V12 = models.FloatField(max_length=250, blank=False, null=False)
    V13 = models.FloatField(max_length=250, blank=False, null=False)
    V14 = models.FloatField(max_length=250, blank=False, null=False)
    V15 = models.FloatField(max_length=250, blank=False, null=False)
    V16 = models.FloatField(max_length=250, blank=False, null=False)
    V17 = models.FloatField(max_length=250, blank=False, null=False)
    V18 = models.FloatField(max_length=250, blank=False, null=False)
    V19 = models.FloatField(max_length=250, blank=False, null=False)
    V20 = models.FloatField(max_length=250, blank=False, null=False)
    V21 = models.FloatField(max_length=250, blank=False, null=False)
    V22 = models.FloatField(max_length=250, blank=False, null=False)
    V23 = models.FloatField(max_length=250, blank=False, null=False)
    V24 = models.FloatField(max_length=250, blank=False, null=False)
    V25 = models.FloatField(max_length=250, blank=False, null=False)
    V26 = models.FloatField(max_length=250, blank=False, null=False)
    V27 = models.FloatField(max_length=250, blank=False, null=False)
    V28 = models.FloatField(max_length=250, blank=False, null=False)
    Amount = models.FloatField(max_length=250, blank=False, null=False)
    
    class Meta:
        db_table = 'manual_input'