# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']

class Location(models.Model):
    location= models.CharField(max_length =30)
   
    def __str__(self):
         return self.location
    class Meta:
        ordering = ['location']

class Image(models.Model):
    post = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    
    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def search_by_category(cls,search_term):
        gallery= cls.objects.filter(category__category__contains=search_term)
        return gallery 
    
    # @classmethod
    # def filter_by_location(cls, id):
    #    gallery = Image.objects.filter(location_id=id)
    #    return gallery