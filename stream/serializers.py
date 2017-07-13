from rest_framework import serializers
from .models import Twitch, Mixer


class TwitchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=False, max_length=24)
    add_date = serializers.DateTimeField(read_only=True)
    partner = serializers.BooleanField(required=False)
    banned = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Twitch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.add_date = validated_data.get('add_date', instance.add_date)
        instance.partner = validated_data.get('partner', instance.partner)
        instance.banned = validated_data.get('banned', instance.banned)
        instance.save()
        return instance
