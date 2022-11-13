from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogTag(models.Model):
    name = models.CharField('Name', max_length=60, blank=False, null=False)
    slug = models.SlugField('Slug', editable=False, max_length=180, unique=True, default=timezone.now )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = str(self.name).strip().replace(' ', '-')
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                            verbose_name='Author')
    title = models.CharField('Title', max_length=120, blank=False, null=False)
    slug = models.SlugField('Slug', editable=False, max_length=180, unique=True, default=timezone.now )
    content = models.TextField('Content', max_length=800, blank=False, null=False)
    banner = models.ImageField('Image', upload_to='images/', blank=True,
                                null=True, default='images/defaut_image.png')
    tags = models.ManyToManyField(BlogTag, verbose_name='Tags')
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = str(self.title).strip().replace(' ', '-')
        super().save(*args, **kwargs)
