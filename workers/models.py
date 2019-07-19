from django.db import models

class Worker(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone = models.IntegerField(default=0)
	bio = models.CharField(max_length=100,blank=True)
	photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')

	def __str__(self):
		return self.first_name