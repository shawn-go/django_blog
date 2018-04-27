from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	required_css_class = 'required'

	class Meta:
		model = Post
		fields = ('title', 'abstract', 'body', 'author', 'category',)
