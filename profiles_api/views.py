from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP Methogs as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapper manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
