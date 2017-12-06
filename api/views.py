from django.shortcuts import render
from django.contrib.auth.models import User

from api.models import GuitarChord
from api.serializers import GuitarChordSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets

from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GuitarChordViewSet(viewsets.ModelViewSet):
    """
    This endpoint allows you to fetch information about guitar chords.

    Use this API explorer to test the requests.
    """
    queryset = GuitarChord.objects.all()
    serializer_class = GuitarChordSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)