from django.db import models
from django.contrib import admin

class mypurchase(models.Model):
    Product_name=models.CharField(max_length=15)
    Product_id=models.IntegerField(primary_key=True)
    Price=models.IntegerField()
    Offer=models.FloatField()
    Weight=models.FloatField()
    Quantity=models.IntegerField()
    Total_amount=models.IntegerField()

class mypurchaseAdmin(admin.ModelAdmin):
    list_display=["Product_name","Product_id","Price","Offer","Weight","Quantity","Total_amount"]