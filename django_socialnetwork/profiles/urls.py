from django.urls import path
from .views import profile, update_profile, profile_search



app_name = 'profiles'


urlpatterns = [
    path('profile/search/', profile_search, name='search'),
    path('profile/update/<int:pk>', update_profile, name='update_profile'),
    path('profile/<str:slug>/', profile, name='profile'),
    
    
]