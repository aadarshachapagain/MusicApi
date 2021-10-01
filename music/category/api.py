from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer




class category_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response(serializer.data)



class category_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = CategorySerializer(music)
        return Response(serializer.data)