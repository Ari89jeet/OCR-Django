
from django.db import models



# Create your models here.
class myuploadfile(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

    def delete(self, using=None, keep_parents=False):
        self.myfiles.storage.delete(self.myfiles.name)
        super().delete()


class myuploadfile_excel(models.Model):
    
    myfiles = models.FileField(upload_to="excel")


    def delete(self, using=None, keep_parents=False):
        self.myfiles.storage.delete(self.myfiles.name)
        super().delete()



class PricingRequest(models.Model):

    
    PartNumber = models.CharField(max_length=50, null=False)
    Nomenclature = models.CharField(max_length=20, null=False)
    Quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return f'{self.PartNumber}'
    
