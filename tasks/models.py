from django.db import models
from datetime import datetime, date
from django.utils import timezone
# Create your models here.
something = (
("3","Choose any..."),("2","Completed"),("1","Prioritize"),
)


class Task(models.Model):
	title = models.CharField(max_length=200)
	#complete = models.BooleanField(default=False)
	complete = models.CharField(max_length=6000,choices = something,default='1')
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title


	