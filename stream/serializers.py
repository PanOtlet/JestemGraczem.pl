from rest_framework import serializers
from .models import Twitch


class TwitchSerializer(serializers.HyperlinkedModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='twitchapi', format='html')

    class Meta:
        model = Twitch
        fields = ('id', 'name', 'add_date', 'partner', 'banned', 'owner_id')
