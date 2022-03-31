from django import forms
from .models import Comment


class FormsComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post" , "date"]
        labels = {
            "user_name" : "Your Name",
            "text" : "Your Comment",
            "email" : "Your Email"
        }


