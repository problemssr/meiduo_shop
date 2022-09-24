from rest_framework import serializers

from apps.goods.models import SKU


class SKUModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'
