from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	auther = models.ForeignKey(User, on_delete= models.CASCADE)
	body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='blog_post')
	category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
	# category = models.CharField(max_length=225, default='uncategories')

	def total_likes(self):
		return self.likes.count()
		
	def __str__(self):
		return self.title + " | " + str(self.auther)

	def get_absolute_url(self):
		# return reverse('article-detail', args=(str(self.id)))
		return reverse('home')