from rest_framework import serializers

from .models import BucketList

class BucketListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE

    class Meta:

        model = BucketList
        fields = ('id', 'name', 'owner', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')
