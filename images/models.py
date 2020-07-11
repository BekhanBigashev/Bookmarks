from django.conf import settings
from django.db import models
from django.utils.text import slugify



class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'images_createed', on_delete = models.CASCADE)
	title = models.CharField(max_length=25)
	slug = models.SlugField(max_length=200, blank=True)
	url = models.URLField()
	image = models.ImageField(upload_to='images/%y/%m/%d')
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add = True, db_index=True)
	user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True)

	def __str__(self):
		return self.title

	def slugify(self):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Image, self).save(*args, **kwargs)


