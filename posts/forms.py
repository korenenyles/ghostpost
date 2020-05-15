from django import forms
from posts.models import PostItem

class AddPost(forms.ModelForm):
    class Meta:
        model = PostItem
        #Matt Perry suggested that boast_or_roast go into fields, rather than declaring it outside of meta to fix bug! 
        fields = ['post_title', 'body', 'boast_or_roast']
    