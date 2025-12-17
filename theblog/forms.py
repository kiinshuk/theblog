from django import forms
from .models import Post, Category

# choices = Category.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
# 	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','category', 'snippet' , 'body', 'header_image')

		widgets = {
		'title': forms.TextInput(attrs={'class': 'from-control' }),
		# 'auther': forms.Select(attrs={'class': 'from-control'}),
		'category': forms.Select(attrs={'class': 'from-control'}),
		'body': forms.Textarea(attrs={'class': 'from-control'}),
		'snippet': forms.TextInput(attrs={'class': 'from-control'}),
		}

