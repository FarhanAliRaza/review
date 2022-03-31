import random
import os
from statistics import mode
from django.db import models

from accounts.models import User
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


from django.utils import timezone

def get_filename_ext(filepath):

    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):

    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "images/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )




class Customer(models.Model):
    
    image = models.ImageField(upload_to=upload_image_path, blank=True)
    feel = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.store_id} + {self.feel}"



class Store(models.Model):
    name = models.CharField(max_length=255, default="name")
    logo = models.ImageField(upload_to=upload_image_path, blank = True, null = True)
    happy = models.PositiveIntegerField(default=0)
    satisfied = models.PositiveIntegerField(default=0)
    neutral = models.PositiveIntegerField(default=0)
    sad = models.PositiveIntegerField(default=0)
    customer = models.ManyToManyField(Customer, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

