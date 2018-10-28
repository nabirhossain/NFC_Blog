from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class author(models.Model):
    auth_name = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_image = models.FileField()
    auth_details = models.TextField()

    def __str__(self):
        return self.auth_name.username

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
       '''select only published posts'''
       return super(PublishedManager, self).get_queryset().filter(status="published")

class post(models.Model):
    post_author = models.ForeignKey(author, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    post_body = RichTextUploadingField()
    post_image = models.FileField()
    post_category = models.ForeignKey(category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # the default manager


    published_objects = PublishedManager()  # The publish-specific manager.

    class Meta:
        ordering = ['-posted_on', ]

    def __str__(self):
        return self.post_title






