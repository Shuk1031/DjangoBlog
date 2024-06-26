from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)