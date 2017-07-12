from inventory.models import Machine
from rest_framework import serializers


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
