from django.shortcuts import render
from rest_framework import generics, permissions

from .models import BucketList
from .serializers import BucketListSerializer
from .permissions import IsOwner
# Create your views here.

class CreateView(generics.ListCreateAPIView):

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
