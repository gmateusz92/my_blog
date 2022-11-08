from django import forms
from .models import Topics, Comment, Calculator

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['title', 'description', ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CalculateForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = ['value_1', 'value_2']

    def calculate(self, value_1, value_2):
        result = value_1 + value_2
        return result


class CalculateForm(forms.Form):
    value_1 = forms.IntegerField()
    value_2 = forms.IntegerField()
