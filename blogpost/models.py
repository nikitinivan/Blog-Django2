from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Custom manager for retrieving posts from db
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, related_name='blog_posts', on_delete='CASCADE')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
            max_length=10,
            choices=STATUS_CHOICES,
            default='draft'
        )

    # Managers:
    objects = models.Manager() # Default Manager
    published = PublishedManager() # Custom manager 

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
