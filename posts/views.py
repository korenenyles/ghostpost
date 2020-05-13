from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import PostItem
# Create your views here.
def index(request):
    data = PostItem.objects.all()
    return render(request, 'index.html',{'data':data})

def post_detail(request, id):
    post = PostItem.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def like_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.likes += 1
    post.save()
    
    return render(request, 'index.html',)