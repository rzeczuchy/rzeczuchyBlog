from django.contrib import admin
from .models import Post

admin.site.site_header = "rzeczuchyBlog admin"
admin.site.site_title = "rzeczuchyBlog admin"

# Register your models here.
admin.site.register(Post)