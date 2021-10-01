from rest_framework import serializers
from .models import Music
from .category.serializers import CategorySerializer
from .genre.serializers import GenreSerializer


class MusicSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = [
            'id',
            'title',
            'author',
            'short_desc',
            'long_desc',
            'main_file',
            'thumbnail_img',
            'bgrnd_vid',
            'categories',
            'genres'
        ]
