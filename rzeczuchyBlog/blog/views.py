from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# Create your views here.
def index(request):
   post_list = Post.objects.order_by('-published_time')
   context = {'post_list': post_list}
   return render(request, 'blog/index.html', context)

class PostDetail(DetailView):
   model = Post
   template_name = 'blog/post_detail.html'