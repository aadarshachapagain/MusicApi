from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre
from .serializers import GenreSerializer




class genre_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Genre.objects.all()
        serializer = GenreSerializer(snippets, many=True)
        return Response(serializer.data)



class genre_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = GenreSerializer(music)
        return Response(serializer.data)