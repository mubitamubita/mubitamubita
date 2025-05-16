from django.db import models
from django.utils.text import slugify



class Publication(models.Model):
  TYPES = (
    ('flash','Flash'),
    ('story','Story'),
    ('poem','Poem'),
    ('novel','Novel'),
    )
  
  title = models.CharField(max_length = 100)
  publication_type = models.CharField(max_length = 100, choices = TYPES)
  magazine = models.CharField(max_length = 100)
  publication_date = models.DateTimeField()
  description = models.TextField(blank = True)
  link = models.URLField(blank = True)
  slug = models.SlugField(unique = True, blank = True)
  created_at = models.DateTimeField(auto_now_add = True)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.title} - {self.magazine}")
    super().save(*args, **kwargs)