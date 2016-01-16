from django.db import models

class Task(models.Model):
	pass

class Question(models.Model):
	user      = models.CharField(max_length=20)
	title     = models.CharField(max_length=100)
	statement = models.CharField(max_length=3000)
	answer    = models.CharField(max_length=3000)
	labes     = models.CharField(max_length=500)
	def __str__(self):
		return '%s %s' % (self.user, self.title)
	class Admin:
		list_display  = ('user', 'title', 'labels')

class Hack(models.Model):
	user      = models.CharField(max_length=20)
	title     = models.CharField(max_length=100)
	statement = models.CharField(max_length=3000)
	resources = models.CharField(max_length=1000)
	techs     = models.CharField(max_length=1000)
	labes     = models.CharField(max_length=500)
	def __str__(self):
		return '%s %s' % (self.user, self.title)
	class Admin:
		list_display  = ('user', 'title', 'labels')

class Article(models.Model):
	user        = models.CharField(max_length=20)
	title       = models.CharField(max_length=100)
	intro       = models.CharField(max_length=500)
	description = models.CharField(max_length=3000)
	basics  = models.CharField(max_length=3000)
	code    = models.CharField(max_length=3000)
	content = models.CharField(max_length=3000)
	problems = models.CharField(max_length=1000)
	labels   = models.CharField(max_length=500)
	def __str__(self):
		return '%s %s' % (self.user, self.title)
	class Admin:
		list_display  = ('user', 'title', 'labels')
