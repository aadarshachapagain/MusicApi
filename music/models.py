from django.db import models
from .category.models import Category
from .genre.models import Genre


# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    short_desc = models.CharField(max_length=200, null=True)
    long_desc = models.TextField(blank=True, null=True)
    main_file = models.FileField(upload_to='music/')
    thumbnail_img = models.ImageField(upload_to='thumbnail/')
    bgrnd_vid = models.FileField(upload_to='bgrnd_video/')
    categories = models.ManyToManyField(Category)
    genres = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title

    # cat (many to many field here category--> music , story)

    class Meta:
        verbose_name_plural = "Music"
