from django.urls import path
from .views import home
from .views import stories
from .views import publications
from .views import contact
from .views import about
from .views import story_detail


urlpatterns = [
  path('', home, name = "home"),
  path('stories/', stories, name = "stories"),
  path('publications/', publications, name = "publications"),
  path('contact/', contact, name = "contact"),
  path('about/', about, name = "about"),
  path('story/<slug:slug>/', story_detail, name = "story"),
  ]
  
  
  
  # sitemap
# from django.contrib.sitemaps.views import sitemap
# from django.contrib.sitemaps import Sitemap
# from .models import Story
# 
# class StorySitemap(Sitemap):
#     def items(self):
#         return Story.objects.all()
# 
# sitemaps = {'stories': StorySitemap}
# 
# urlpatterns = [
#     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
# ]