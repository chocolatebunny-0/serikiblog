from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
 
    upload = models.ImageField(upload_to ='uploads/') 

    title = models.CharField(max_length=250, null=True)
    excerpt = models.TextField(null=True)

    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager
    slug = models.SlugField(max_length = 150, unique=False)

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.property_Name, allow_unicode=True)
        
        
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title