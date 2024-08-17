from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.SlugField() # to create human-friendly urls

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single', kwargs={'pk': self.id, 'slug': self.slug})