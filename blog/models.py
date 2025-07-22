from django.db import models
from django.utils.text import slugify
class Blog(models.Model):
    title=models.CharField(max_length=500, default='')
    content=models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='General')
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)