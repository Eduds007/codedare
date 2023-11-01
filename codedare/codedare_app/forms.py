from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'  
        exclude = ['author', 'date']

class PostFilterForm(forms.Form):
    filter = forms.CharField(required=False)
    
