from rest_framework import serializers, status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response

from api.models import Song, Audiobook, Podcast


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

    def validate_participants(self, value=None):
        if value is not None:
            list_data = value.split(',')
            if len(list_data) > 10:
                raise Exception('maximum of 10 participants possible')
            for i in list_data:
                if len(i) > 100:
                    raise Exception('participant name not greater than 100 characters')
        return value


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'
