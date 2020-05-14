from django import forms
from posts.models import PostItem

class AddPost(forms.ModelForm):
    class Meta:
        model = PostItem
        fields = ['post_title', 'body', 'boast_or_roast']
    