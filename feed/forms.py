from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "text"]
        labels = {
            "text": "Description",  # Replace with your desired label
        }