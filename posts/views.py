from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import PostItem
from posts.forms import AddPost
# Create your views here.
def index(request):
    data = PostItem.objects.order_by('-date')
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'index.html',{'form':form,'data':data})

def post_detail(request, id):
    post = PostItem.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

def boast_view(request):
    data = PostItem.objects.filter(boast_or_roast=True).order_by('-date')
    return render(request, 'index.html', {'data':data})

def roast_view(request):
    data= PostItem.objects.filter(boast_or_roast=False).order_by('-date')
    return render(request, 'index.html', {'data':data})

def vote_view(request):
    data = PostItem.objects.order_by('-results')
    return render(request, 'index.html', {'data':data})

def like_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.results +=1
    post.save()
    return HttpResponseRedirect(reverse('post_detail', kwargs={'id': post_id}))

def dislike_view(request, post_id):
    post = PostItem.objects.get(id = post_id)
    post.results -= 1
    post.save()
    return HttpResponseRedirect(reverse('post_detail', kwargs={'id': post_id}))


