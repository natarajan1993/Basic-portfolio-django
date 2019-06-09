from django.urls import path
from .views import *

urlpatterns = [
    path('', all_blogs, name='all-blogs'),
    path('<int:blog_id>', detail, name='detail')
]
