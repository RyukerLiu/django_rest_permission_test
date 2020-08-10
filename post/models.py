from django.db import models

# Create your models here.
class Post(models.Model):
    topic = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        ordering = ['created_at']