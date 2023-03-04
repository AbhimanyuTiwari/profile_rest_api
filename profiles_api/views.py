from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return  a list  of ApiView features"""
        apiView = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to tradition Django View',
            'Gives the more control over your application logic'
            'Is mapped manually to URL'
        ]

        return Response({"message": 'Hello!', "apiView": apiView})
