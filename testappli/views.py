# PYTHON
# DJANGO
# DJANGO (THIRD PARTIES)
from rest_framework import viewsets, permissions, status, serializers
# FULLPLANNER
from testappli.models import Parent, Child
from testappli.serializers import ParentSerializer, ChildSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)