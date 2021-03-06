from django.db import models

# Create your models here.


class Contact_table(models.Model):
	Name = models.CharField(max_length=200)
	Mobile = models.CharField(max_length=13)
	Email = models.EmailField(max_length=70,blank=True)
	Subject = models.CharField(max_length=200)
	Message = models.CharField(max_length=1000)

