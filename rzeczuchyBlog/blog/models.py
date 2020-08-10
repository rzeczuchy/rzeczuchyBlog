from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    published_time = models.DateTimeField('published at')
    author = models.CharField(max_length=50)
    main_content = models.TextField(max_length=2500)

    def __str__(self):
        return self.title