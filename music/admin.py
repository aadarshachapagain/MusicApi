from django.contrib import admin
from .models import Music
from .category.models import Category
from .genre.models import Genre


# Register your models here.




admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Genre)
