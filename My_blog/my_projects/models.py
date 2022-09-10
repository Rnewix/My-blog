from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Projects(models.Model):         
    id = models.AutoField(primary_key=True)                                                          
    name = models.CharField(max_length=25)
    url= models.URLField()
    description= models.TextField(null=True, max_length=1000)
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        showname= self.name + ' -- ' + self.description  
        return showname    
    
#    def delete(self, using=None, keep_parents=False):
#        self.image.storage.delete(self.image.id)
#        super().delete()