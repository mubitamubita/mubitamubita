from django.contrib import admin
from stories.models import Story
from .models import Publication
from stories.models import Book
from stories.models import BigBook

admin.site.register(Story)
admin.site.register(Publication)
admin.site.register(Book)
admin.site.register(BigBook)

