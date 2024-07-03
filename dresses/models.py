from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Dress(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    # image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return self.description
    
class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    dress = models.ForeignKey(Dress, on_delete=models.SET_NULL, null=True, blank=False)
    first_pic = models.BooleanField(null=False, blank=False)
    
    def __str__(self):
        return str(self.dress)