from django import forms
from .models import Post # from the post model

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)