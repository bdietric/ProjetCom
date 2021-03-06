from django import forms
from .models import Form,FieldForm

class PollForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('title','password')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = FieldForm
        fields = ('question',)
