from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permisssions

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer
        

    def get(self, request, format=None):
        """Return  a list  of ApiView features"""   
        apiView = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to tradition Django View',
            'Gives the more control over your application logic'
            'Is mapped manually to URL'
        ]

        return Response({"message": 'Hello!', "apiView": apiView})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test View Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a list"""

        a_viewset=[
            "Uses action (list, update, create, retrive, pratial_update)",
            "Automatically maps Urls to Routors",
            "Provide more functionality with less code"
        ]

        return Response({"message":"Hello!","a_viewset":a_viewset})
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permisssions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)