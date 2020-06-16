from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Todo
        fields = ('id', 'description')
