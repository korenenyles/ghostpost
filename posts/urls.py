from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),
    path('like/<int:post_id/>', views.like_view),
]

