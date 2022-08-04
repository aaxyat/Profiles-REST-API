from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Testing APIview"""
    name = serializers.CharField(max_length=10)