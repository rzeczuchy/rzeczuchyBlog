from django.urls import path
from . import views
from .views import PostDetail
 
app_name = 'blog'
urlpatterns = [
   path('', views.index, name="index"),
   path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
]
