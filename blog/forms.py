from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


        widgets = {
          'text': forms.Textarea(
                                  attrs={'placeholder':"Write your comment",
                                         'class':"comment-form-text"}
                                 ),
            'author': forms.TextInput(
                attrs={'placeholder': "Name",
                       'class':"comment-form-author"}
            ),
        }
