from django.contrib.auth.models import User, Group
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import permissions, viewsets
from rest_framework import generics

from lists.serializers import UserSerializer, GroupSerializer

# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope] 
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#
#class GroupViewSet(viewsets.ModelViewSet):
#    permission_classes = [permissions.IsAuthenticated, TokenHasScope] 
#    required_scopes = ['groups']
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer


class UserList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
