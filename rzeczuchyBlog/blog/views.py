from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def index(request):
   post_list = Post.objects.order_by('-published_time')
   paginator = Paginator(post_list, 3)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'blog/index.html', {'page_obj': page_obj})

class PostDetail(DetailView):
   model = Post
   template_name = 'blog/post_detail.html'

def about(request):
   return render(request, 'blog/about.html')