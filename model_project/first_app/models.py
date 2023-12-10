from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length= 10)
    roll = models.IntegerField(primary_key= True)
    address = models.TextField(null= True)
    father_name= models.TextField(null= True)
    
    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"