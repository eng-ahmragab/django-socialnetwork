from django import forms

from .models import Post, Comment



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
    
    # customize form fields 
    content_attrs = {
        'placeholder': 'Write something awesome ...',
        'rows': 2
    }
    content = forms.CharField(
        widget=forms.Textarea(attrs=content_attrs), 
        label='',
    )
    image = forms.ImageField(label='', required=False)





class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    
    # customize form fields 
    content_attrs = {
        'placeholder': 'Add a comment ...',
        'rows': 1,
        'class': 'form-control comment-input',
    }
    content = forms.CharField(
        widget=forms.Textarea(attrs=content_attrs), 
        label='',
    )