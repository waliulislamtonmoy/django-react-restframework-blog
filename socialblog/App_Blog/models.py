from django.db import models
from autoslug import AutoSlugField
# Create your models here.

from App_Account.models import UserProfile

blog_category = (
    ("IT", "IT"),
    ("FICTION", "FICTION"),
    ("APP", "APP"),
    ("SECURITY", "SECURITY"),
    ("TECH", "TECH"),
    ("AI", "AI"),
    ("BLOG","BLOG"),
)

class Blog(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    content = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=30,choices=blog_category,default="BLOG")
    image=models.ImageField( upload_to="blogimage/", null=True,blank=True)
    date=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    