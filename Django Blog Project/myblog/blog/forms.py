from django.forms import Textarea
from .models import Comment
from django import forms


class AddCommentForm(forms.ModelForm):
    content = Textarea()

    class Meta:
        model = Comment
        fields = ['content']
