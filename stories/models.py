from django.db import models
from django.utils.text import slugify

class Story(models.Model):
  GENRE = (
    ('horror','Horror'),
    ('action','Action'),
    ('Fantansy','Fantasy'),
    ('romance','Romance'),
    )
  title = models.CharField(max_length = 50)
  pub_date = models.DateTimeField(auto_now_add = True)
  genre = models.CharField(max_length = 100, choices = GENRE)
  content = models.TextField()
  dedication = models.TextField(blank = True, null =True)
  slug = models.SlugField(unique = True, blank = True)
  link = models.URLField(blank = True)
  


  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)
    

class Book(models.Model):
  GENRE = (
    ('horror','Horror'),
    ('action','Action'),
    ('Fantansy','Fantasy'),
    ('romance','Romance'),
    )
    
  cover = models.ImageField(upload_to ="covers/" , default = "covers/default.jpg")
  title = models.CharField(max_length = 100)
  publication_date = models.DateTimeField()
  genre = models.CharField(max_length = 100, choices = GENRE)
  price = models.DecimalField(max_digits = 5, decimal_places = 2)
  description = models.TextField()
  link = models.URLField(blank = True)
  
class BigBook(models.Model):
  GENRE = (
    ('horror','Horror'),
    ('action','Action'),
    ('Fantansy','Fantasy'),
    ('romance','Romance'),
  )
    
  cover = models.ImageField(upload_to ="covers/" , default = "covers/default.jpg")
  title = models.CharField(max_length = 100)
  publication_date = models.DateTimeField()
  genre = models.CharField(max_length = 100, choices = GENRE)
  price = models.DecimalField(max_digits = 5, decimal_places = 2)
  description = models.TextField()
  link = models.URLField(blank = True)