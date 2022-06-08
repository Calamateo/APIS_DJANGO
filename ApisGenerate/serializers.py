from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers 
from ApisGenerate.models import (
    OmniClass23, 
    OMC23Nivel1, 
    OMC23Nivel2,
    OMC23Nivel3,
    OMC23Nivel4,
    OMC23Nivel5,
    OMC23Nivel6,
    ) 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email','groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'url']
        
        
class OmniClass23Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OmniClass23
        fields = ['idOmc23', 'numMat', 'Codigo', 'descriEng', 'descriSpa', 'Nivel', 'regFinal']

class OMC23Nivel1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel1
        fields = [ 'idOmc23N1', 'Codigo', 'descriSpa', 'descriEng']


class OMC23Nivel2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel2
        fields = [ 'idOmc23N2', 'Codigo', 'descriSpa', 'descriEng','fk_Omc23N1']

class OMC23Nivel3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel3
        fields = [ 'idOmc23N3', 'Codigo', 'descriSpa', 'descriEng', 'fk_Omc23N2']
    
class OMC23Nivel4Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel4
        fields = [ 'idOmc23N4', 'Codigo', 'descriSpa', 'descriEng', 'fk_Omc23N3']
    
class OMC23Nivel5Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel5
        fields = [ 'idOmc23N5', 'Codigo', 'descriSpa', 'descriEng', 'fk_Omc23N4']
    
class OMC23Nivel6Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OMC23Nivel6
        fields = [ 'idOmc23N6', 'Codigo', 'descriSpa', 'descriEng', 'fk_Omc23N5']
    