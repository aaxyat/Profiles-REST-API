from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ViewSet

from profiles_api import serializers, models
from profiles_api import permissions

class HelloApiView(APIView):
    """Hello World"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """ test APIview """

        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a Hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({message: message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        "Partial Update"
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self,request):
       a_viewset = [
           'Uses HTTP methods as function(get, post, patch, put, delete)',
           'Is similar to a traditional Django View',
           'Gives you the most control over your application logic',
           'Is mapped manually to URLs',
       ]
       return Response({'message': 'Hello!', 'a_viewset': a_viewset}, status=status.HTTP_200_OK)


    def retrive(self, request, pk=None):
       return Response({'http.method': 'GET'})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({message: message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response({'http.method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        return Response({'http.method': 'PARTIAL_UPDATE'})

    def destroy(self, request, pk=None):
        return Response({'http.method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """manage CRUD of Profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)