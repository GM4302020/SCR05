from django.db import models
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField('Title', max_length=120, blank=False, null=False)
    content = models.TextField('Content', max_length=800, blank=False, null=False)

    def __str__(self) -> str:
        return self.title
        
    
