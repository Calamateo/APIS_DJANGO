from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ApisGenerate.serializers import (
    UserSerializer, 
    GroupSerializer, 
    OmniClass23Serializer, 
    OMC23Nivel1Serializer, 
    OMC23Nivel2Serializer,
    OMC23Nivel3Serializer,
    OMC23Nivel4Serializer,
    OMC23Nivel5Serializer,
    OMC23Nivel6Serializer,
    )
from ApisGenerate.models import (
    OmniClass23, 
    OMC23Nivel1, 
    OMC23Nivel2,
    OMC23Nivel3,
    OMC23Nivel4,
    OMC23Nivel5,
    OMC23Nivel6,
    )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class OmniClass23ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OmniClass23.objects.all()
    serializer_class = OmniClass23Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel1ViewSet(viewsets.ModelViewSet):
    queryset =OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC23Nivel2ViewSet(viewsets.ModelViewSet):
    queryset =OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC23Nivel3ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel4ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel5ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel6ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]