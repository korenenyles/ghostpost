from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),
    path('like/<int:post_id>/', views.like_view),
    path('dislike/<int:post_id>/', views.dislike_view),
      path('boast/', views.boast_view, name='boast'),
    path('roast/', views.roast_view, name='roast'),
    path('vote/', views.vote_view, name='votes')

]

