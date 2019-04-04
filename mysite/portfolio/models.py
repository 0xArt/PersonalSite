from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class AnalogProject(models.Model):
	title = models.CharField(max_length = 140)
	summary = RichTextUploadingField()
	tags = models.CharField(max_length = 400)
	cover_image = models.ImageField(upload_to='cover_image', blank=True)
	blog_link = models.CharField(max_length = 140, default='')

	def __str__(self):
		return self.title
		
	def tags_list(self):
		return self.tags.split(', ')
		
class DigitalProject(models.Model):
	title = models.CharField(max_length = 140)
	summary = RichTextUploadingField()
	tags = models.CharField(max_length = 400)
	cover_image = models.ImageField(upload_to='cover_image', blank=True)
	blog_link = models.CharField(max_length = 140, default='')


	def __str__(self):
		return self.title
		
	def tags_list(self):
		return self.tags.split(', ')