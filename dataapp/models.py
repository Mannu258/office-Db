from django.db import models


class mojo(models.Model):
    Item_Code = models.IntegerField(null=False)
    Item_name = models.CharField(max_length=60,default = " ",null  = True)
    Raw_Material = models.CharField(max_length=60,default = " ",null  = True)
    Category = models.CharField(max_length=60,default = " ",null  = True)
    Material_Content = models.CharField(max_length=60,default = " ",null  = True)
    Color = models.CharField(max_length=60,default = " ",null  = True)
    Design_Print_GG = models.CharField(max_length=60,default = " ",null  = True)
    Width = models.CharField(max_length=60,default = " ",null  = True)
    Count = models.CharField(max_length=60,default = " ",null  = True)
    Thickness = models.CharField(max_length=60,default = " ",null  = True)
    GSM = models.CharField(max_length=60,default = " ",null  = True)
    Micron = models.CharField(max_length=60,default = " ",null  = True)
    Size = models.CharField(max_length=60,default = " ",null  = True)
    Weight_Kgs = models.CharField(max_length=60,default = " ",null  = True)
    QTY = models.CharField(max_length=60,default = " ",null  = True)
    QTY_MTR = models.CharField(max_length=60,default = " ",null  = True)
    Category_End_use = models.CharField(max_length=60,default = " ",null  = True)
    OLD_Code = models.CharField(max_length=60,default = " ",null  = True)
    Source_vendor_detail = models.CharField(max_length=60,default = " ",null  = True)
    date = models.CharField(max_length=60,default = " ",null  = True)
    Price =  models.CharField(max_length=60,default = " ",null  = True)
    Qty_G  = models.CharField(max_length=60,default = " ",null  = True)
    GST= models.CharField(max_length=60,default = " ",null  = True)
    Received_Date = models.CharField(max_length=60,default = " ",null  = True)
    Recived_by  = models.CharField(max_length=60,default = " ",null  = True)
    Vendor_Code = models.CharField(max_length=60,default = " ",null  = True)
    Remark = models.CharField(max_length=60,default = " ",null  = True)
    images = models.ImageField(upload_to="mojoimages",null=True)

    def __str__(self) -> str:
        return '%s'%self.Item_Code
    
