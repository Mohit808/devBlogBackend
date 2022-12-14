from django.db import models

# Create your models here.
class devBlog(models.Model):
    uniqueKeys=models.CharField(max_length=200,default="")
    title=models.CharField(max_length=200,default="")
    code=models.CharField(max_length=200,default="")
    class Meta:
        db_table="devBlog"


class StripeDb(models.Model):
    email=models.CharField(max_length=200,default="",primary_key=True)
    accountId=models.CharField(max_length=100,default="")
    class Meta:
        db_table="StripeDb"

class StripeServiceDb(models.Model):
    email=models.CharField(max_length=200,default="")
    accountId=models.CharField(max_length=100,default="")
    serviceName=models.CharField(max_length=200,default="")
    amount=models.CharField(max_length=200,default="")
    class Meta:
        db_table="StripeServiceDb"

