from rest_framework import serializers
from sembadaapi.models import Sembadaapi

class SembadaapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sembadaapi
        fields = "__all__"