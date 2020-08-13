from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    published_time = models.DateTimeField('published at')
    author = models.CharField(max_length=50)
    main_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title