from rest_framework import serializers
from api.models import GuitarChord

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    guitar_chords = serializers.HyperlinkedRelatedField(many=True, view_name='api:guitarchord-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'guitar_chords')

class GuitarChordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GuitarChord
        fields = ('id', 'owner', 'name', 'modifier', 'capo', 'high_e_string', 'high_e_string_finger', 
            'b_string', 'b_string_finger', 'g_string', 'g_string_finger', 'd_string', 'd_string_finger', 
            'a_string', 'a_string_finger', 'low_e_string', 'low_e_string_finger', 'image',)
