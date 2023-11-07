from rest_framework import serializers
from ...core.loading import get_model

TABLE = get_model('requests', 'Request')
APP = 'requests_api'
fields = ('id', 'name', 'description', 'langitute', 'latitude', 'author', 'created_at', 'updated_at')


class RequestsSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name=APP + ':update')
    delete_url = serializers.HyperlinkedIdentityField(view_name=APP + ':delete')

    class Meta:
        model = TABLE
        fields = fields + ('update_url', 'delete_url')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.langitute = validated_data.get('langitute', instance.langitute)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()

        return instance


class RequestsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TABLE
        fields = fields

    def create(self, validated_data):
        TABLE.objects.create(**validated_data)
        return validated_data
