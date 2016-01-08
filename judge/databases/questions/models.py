from django.db import models

# Create your models here.

class Question(models.Model):
	user = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=1000)
	def __str__(self):
		return '%s %s' % (self.user, self.title)
