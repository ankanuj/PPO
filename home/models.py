from django.db import models
class ppo(models.Model):
	img_1 = models.ImageField(upload_to='photos/%y/%m/%d/')
	img_2 = models.ImageField(upload_to='photos/%y/%m/%d/')
	img_3 = models.ImageField(upload_to='photos/%y/%m/%d/')
