from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class tag(models.Model):
	name = models.CharField(max_length=50, unique=True)


	class Meta:
		verbose_name = 'tag'
		verbose_name_plural = 'tags'
		ordering = ['name']


class Bookmark(models.Model):
	url = models.URLField()
	title = models.CharField('title', max_length='255')
	description = models.CharField('description', blank=True)
	is_public = models.BooleanField('public', default=True)
	date_created = models.DateTimeField('date created')
	date_updated = models.DateTimeField('date updated')
	owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
	tags = models.ManytoManyField(Tag, blank=True)

	class Meta:
		verbose_name = 'bookmark'
		verbose_name_plural = 'bookmarks'
		ordering = ['-date_created']
