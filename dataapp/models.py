from django.db import models

# Create your models here.

class mojo(models.Model):
    Item_Code = models.IntegerField(null=False)
    Item_name = models.CharField(max_length=60,default = " ")
    Color = models.CharField(max_length=60,default = " ")
    width = models.CharField(max_length=60,default = " ")
    GSM_Size = models.CharField(max_length=60,default = " ")
    Weight_KGS = models.CharField(max_length=60,default = " ")
    Qty = models.CharField(max_length=60,default = " ")
    Material_Content = models.CharField(max_length=60,default = " ")
    Category_End_use = models.CharField(max_length=60,default = " ")
    OLD_Code = models.CharField(max_length=60,default = " ")
    Source_vendor_detail = models.CharField(max_length=60,default = " ")
    Date = models.CharField(max_length=60,default = " ")
    PRICE = models.CharField(max_length=60,default = " ")
    GST = models.CharField(max_length=60,default = " ")
    Thickness = models.CharField(max_length=60,default = " ")
    Received_Date = models.CharField(max_length=60,default = " ")
    Received_BY = models.CharField(max_length=60,default = " ")
    Vendor_Code	 = models.CharField(max_length=60,default = " ")
    Remarks = models.CharField(max_length=60,default = " ")
    Design_Print_GG = models.CharField(max_length=60,default = " ")
    Qty_in_MTR = models.CharField(max_length=60,default = " ")
    Micron = models.CharField(max_length=60,default = " ")
    Count = models.CharField(max_length=60,default = " ")
    Fiber_Length = models.CharField(max_length=60,default = " ")
    Mtr = models.CharField(max_length=60,default = " ")
    Color = models.CharField(max_length=60,default = " ")
    Shade_No = models.CharField(max_length=60,default = " ")
    Style_name = models.CharField(max_length=60,default = " ")
    
