from django.conf import settings
from django.db import models
from django.utils import timezone

class Songs(models.Model):
	album = models.ForeignKey('Albums', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	singer = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	genre	= models.CharField(max_length=200)

	

	class Meta:
		db_table = 'songs'
		app_label = 'musicApp'
    
    
    
    
