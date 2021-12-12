from rest_framework import serializers

from vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


class SetDriverSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.driver_id = validated_data.get('username', instance.username)
        print('instance of username', instance.username)
        return instance

class Meta:
        model = Vehicle
        fields = '__all__'
