from rest_framework import serializers
from .models import Artist

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields='__all__'
