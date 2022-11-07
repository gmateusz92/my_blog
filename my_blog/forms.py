from django import forms
from .models import Topics, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['title', 'description', ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']