from django.urls import path
from .views import index, video_page

urlpatterns = [
    path('', index, name='index'),
    path('video/<str:id>/', video_page, name='video_page')
]
