from django import forms 

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['name', 'email', 'comment']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_added',]