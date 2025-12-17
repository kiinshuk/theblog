from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True,on_delete= models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, null= True, blank = True)
	fb_url = models.CharField(max_length=255, null= True, blank = True)
	twitter_url = models.CharField(max_length=255, null= True, blank = True)
	instagram_url = models.CharField(max_length=255, null= True, blank = True)
	pintrest_url = models.CharField(max_length=255, null= True, blank = True)


	def __str__(self):
		return str(self.user)



# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	auther = models.ForeignKey(User, on_delete= models.CASCADE)
	# body = models.TextField()
	body = RichTextField(blank = True, null= True)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	post_date = models.DateField(auto_now_add=True)
	snippet = models.CharField(max_length=225)
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


