from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_google_maps import fields as map_fields

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.SlugField(unique = True)
    description = models.TextField()
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name='host_profile')
    clicked = models.IntegerField( default = 0)
    date_posted = models.DateTimeField()
    address = models.CharField( max_length = 50 )
    city = models.CharField( max_length = 50 )
    country = models.CharField( max_length = 50 )
    picture1 = models.ImageField()
    picture2 = models.ImageField()
    picture3 = models.ImageField()
    picture4 = models.ImageField()

    def is_clicked(self):
        self.clicked += 1
        self.save()


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


