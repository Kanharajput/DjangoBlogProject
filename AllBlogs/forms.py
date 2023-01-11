from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment     
        exclude = ["post"]        # use all columns as field except post
        labels = {
                    "user_name":"Your Name",
                    "email_addr":"Email Addr",
                    "text":"Text",
        }