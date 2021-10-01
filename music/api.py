from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from .models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response






class music_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Music.objects.all()
        serializer = MusicSerializer(snippets, many=True)
        return Response(serializer.data)



class music_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)
