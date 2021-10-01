from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.SlugField(unique = True)
    description = models.CharField(max_length = 200)
    host = models.ForeignKey(User, on_delete = models.CASCADE)
    clicked = models.IntegerField( default = 0)
    date_posted = models.DateTimeField()
    address = models.CharField( max_length = 50 )

def create_slug(instance, new_slug = None, id = 0):
    slug = slugify(instance.title.lower())
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug)
    if(qs.exists()):
        new_slug = '%s-%s' %( slugify(instance.title.lower()) , id)
        return create_slug(instance, new_slug = new_slug, id = id+1)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)


