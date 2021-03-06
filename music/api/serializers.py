from rest_framework import serializers

from music.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'description')
