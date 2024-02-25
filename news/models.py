from django.db import models
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news_image/images')
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    uptated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-published_time']
    def get_absolute_url(self):
        return reverse('news_detail_page', args=[self.id])
    def __str__(self):
        return self.title
