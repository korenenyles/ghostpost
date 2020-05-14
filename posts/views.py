from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import PostItem
from posts.forms import AddPost
# Create your views here.
def index(request):
    data = PostItem.objects.all()
    return render(request, 'index.html',{'data':data})

def post_detail(request, id):
    post = PostItem.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def add_post(request):
    html = "generic_form.html"
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("home"))

    return render(request, html, {"form": form})

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


