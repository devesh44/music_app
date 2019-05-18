from django.conf import settings
from django.db import models
from django.utils import timezone

class Albums(models.Model):
	title = models.CharField(max_length=200)
	number_of_song = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	singer = models.CharField(max_length=200)

	



	class Meta:
		app_label = 'musicApp'
		db_table = 'albums'
		
