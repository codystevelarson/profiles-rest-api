from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from . import serializers


class HelloApiView(APIView):
    ''' Test API View '''

    # Sets what serializer class to use
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' Returns a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as functions (GET, POST, PUT, PATCH, DELETE)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        ''' Create a hello message with our name'''
        # Formats/Serializes the data in the request to our serializer class format
        serializer = self.serializer_class(data=request.data)

        # Use serializer class validation on new object
        if serializer.is_valid():
            # Get name from validated data
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        # Return the errors from the serializer validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        ''' Handle updating an object '''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        ''' Handle a partial update of an object '''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        ''' Delete an Object '''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    ''' Test API ViewSet '''

    serialzer_class = serializers.HelloSerializer

    def list(self, request):
        ''' Return a hello message '''
        a_viewset = [
            'Uses actions (List, Create, Retrieve, Update, Patrial_Update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        ''' Create a new hello message '''
        serializer = self.serialzer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        ''' Handle getting an object by id '''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        ''' Handle updating an object '''
        return Response({'http_method': 'PUT'})

    def patrial_update(self, request, pk=None):
        ''' Handle updating part of an object '''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        ''' Handle removing an object '''
        return Response({'http_method': 'DELETE'})
