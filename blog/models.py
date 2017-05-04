#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)

class Tag(models.Model):

    name = models.CharField(max_length=100)
class HeadPhoto(models.Model):

    headp1 = models.URLField()

class Post(models.Model):

    title = models.CharField(max_length=70)
    img_head = models.URLField()
    body = models.TextField()
    img1 = models.URLField(blank=True)
    body2 = models.TextField(blank=True)
    img2 = models.URLField(blank=True)
    body3 = models.TextField(blank=True)
    img3 = models.URLField(blank=True)
    body4 = models.TextField(blank=True)
    img4 = models.URLField(blank=True)
    body5 = models.TextField(blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    class Meta: 
            ordering = ['-modified_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

# create user 
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
        
