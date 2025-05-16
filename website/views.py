from django.shortcuts import render, get_object_or_404
from stories.models import Story
from stories.models import Book
from stories.models import BigBook
from .models import Publication

def home(request):
  books = Book.objects.all()
  promobooks = BigBook.objects.all()
  return render(request, "website/home.html",{'books':books,'promobooks':promobooks})

def stories(request):
  stories = Story.objects.all()
  return render(request, "website/stories.html", {'stories':stories})
  
def publications(request):
  stories = Publication.objects.all()
  return render(request, "website/publications.html", {'stories':stories})

def contact(request):
  return render(request, "website/contact.html")

def about(request):
  return render(request, "website/about.html")
  
def story_detail(request, slug):
  story = get_object_or_404(Story, slug = slug)
  return render(request,"website/story.html",{'story':story})