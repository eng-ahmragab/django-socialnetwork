from django.urls import path
from .views import (
    feed, 
    add_post, 
    PostDeleteView,
    PostUpdateView,
    add_comment, 
    like_unlike_post,
)


app_name = 'feed'

urlpatterns = [
    path('', feed, name='feed'),
    
    path('posts/add/', add_post, name='add_post'),
    path('posts/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('posts/update/', PostUpdateView.as_view(), name='update_post'),
    
    path('comments/add/', add_comment, name='add_comment'),
    
    path('like/', like_unlike_post, name='like'),
    
]