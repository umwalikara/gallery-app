# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt
# Create your tests here.

class ImageTestClass(TestCase):
  
   def setUp(self):
        self.kigali = Location(location='kigali')
        self.kigali.save_location()

   def test_instance(self):
       self.assertTrue(isinstance(self.image, Image))

   def test_save_method(self):
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

   def test_delete_method(self):
      
       self.image.save_image()
       self.image.delete_image()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.techno = Category(category='techno')
        self.techno.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.techno,Category))
    
    def tearDown(self):
        self.techno.delete_category()

class LocationTestClass(TestCase):
    def setUp(self):
        self.kigali = Location(location='kigali')
        self.kigali.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.kigali.id)
        location.update_location('kigali')
        location = Location.get_location_id(self.kigali.id)
        self.assertTrue(location.location == 'kigali')
    
    def tearDown(self):
        self.kigali.delete_location()
