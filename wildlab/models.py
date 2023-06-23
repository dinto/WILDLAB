from django.db import models

# Create your models here.
class News_Update(models.Model):
    Date=models.DateField()
    News_Description=models.CharField(max_length=200)
    
    def __str__(self):
        return self.News_Description

class Publication(models.Model):
    Year=models.IntegerField()
    Publication_Description=models.CharField(max_length=1000)
    DOI=models.CharField(null=True,blank=True,max_length=500)
    PDF_Link=models.CharField(null=True,blank=True,max_length=500)
    
    def __str__(self):
        return self.Publication_Description


        
