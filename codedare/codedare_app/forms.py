from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    coding_language = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )   
    class Meta:
        model = Post
        #fields =  '__all__'
        fields = ['title' , 'content', 'coding_language']
        
        



class PostFilterForm(forms.Form):
    title_filter = forms.CharField(required=False)
    start_date_filter = forms.DateField(
        label='Data Inicial',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    end_date_filter = forms.DateField(
        label='Data Final',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =  ['comment']

class CommentFilterForm(forms.Form):
    start_date_filter = forms.DateField(
        label='Data Inicial',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    end_date_filter = forms.DateField(
        label='Data Final',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
