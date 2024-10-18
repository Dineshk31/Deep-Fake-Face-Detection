from django.db import models

# Create your models here.
# User Model
class USER(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=13)
    
    class Meta:
        verbose_name_plural = "USER" 
        
    def __str__(self):
        return self.full_name